import random


class Character:
	def __init__(self, hp, ac, attack_bonus, damage, dexterity, is_player=False):
		self.is_player = is_player
		self.original_hp = hp
		self.hp = hp
		self.ac = ac
		self.attack_bonus = attack_bonus
		self.damage = damage
		self.dexterity = dexterity
		self.initiative = 0
	
	def is_alive(self):
		return self.hp > 0

	def attack(self, target):
		attack_roll = random.randint(1, 20)
		if attack_roll + self.attack_bonus >= target.ac:
			damage_dealt = random.randint(1, self.damage)
			target.take_damage(damage_dealt)

	def take_damage(self, damage):
		self.hp -= damage


def are_players_alive(combatants):
	return bool(len([combatant for combatant in combatants if combatant.is_alive() and combatant.is_player]))


def are_enemies_alive(combatants):
	return bool(len([combatant for combatant in combatants if combatant.is_alive() and not combatant.is_player]))
	
def main():
	combatants = []
	combatants += [Character(hp=15, ac=15, attack_bonus=4, damage=6, dexterity=16, is_player=True)]
	combatants += [Character(hp=15, ac=15, attack_bonus=4, damage=6, dexterity=16, is_player=True)]
	combatants += [Character(hp=15, ac=15, attack_bonus=4, damage=6, dexterity=16, is_player=True)]
	combatants += [Character(hp=7, ac=13, attack_bonus=3, damage=4, dexterity=12)]
	combatants += [Character(hp=7, ac=13, attack_bonus=3, damage=4, dexterity=12)]
	combatants += [Character(hp=7, ac=13, attack_bonus=3, damage=4, dexterity=12)]
	combatants += [Character(hp=7, ac=13, attack_bonus=3, damage=4, dexterity=12)]
	combatants += [Character(hp=7, ac=13, attack_bonus=3, damage=4, dexterity=12)]
	combatants += [Character(hp=7, ac=13, attack_bonus=3, damage=4, dexterity=12)]

	player_wins = 0
	total_leftover_hp = 0
	max_final_player_hp = 0
	num_simulations = 50000

	for _ in range(num_simulations):
		for combatant in combatants:
			combatant.initiative = random.randint(1, 20) + combatant.dexterity
			initiative_order = combatants
			initiative_order.sort(key=lambda x: x.initiative, reverse=True)
			while are_players_alive(combatants) and are_enemies_alive(combatants):
				alive_combatants = [combatant for combatant in initiative_order if combatant.is_alive()]
				alive_players = [combatant for combatant in alive_combatants if combatant.is_player]
				alive_enemies = [combatant for combatant in alive_combatants if not combatant.is_player]
				for combatant in alive_combatants:
					if combatant.is_player:
						enemy = alive_enemies[random.randint(0, len(alive_enemies)-1)]
						combatant.attack(enemy)
					else:
						player = alive_players[random.randint(0, len(alive_players)-1)]
						combatant.attack(player)

		if are_players_alive(combatants):
			alive_players = [combatant for combatant in alive_combatants if combatant.is_player]
			leftover_hp = 0
			for player in alive_players:
				leftover_hp += player.hp
				if player.hp > max_final_player_hp:
					max_final_player_hp = player.hp
			total_leftover_hp += leftover_hp / len(alive_players)
			player_wins += 1

		# Reset combatants for the next battle
		for combatant in combatants:
			combatant.hp = combatant.original_hp

	# Calculate win percentage
	player_win_percentage = (player_wins / num_simulations) * 100
	average_final_player_hp = total_leftover_hp / num_simulations

	print(f"player win percentage: {player_win_percentage:.2f}%")
	print(f"average final player hp: {average_final_player_hp:.2f}")
	print(f"max final player hp: {max_final_player_hp}")


main()
