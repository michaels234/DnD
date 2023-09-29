import random


class Character:
	def __init__(self, hp, ac, attack_bonus, damage, dexterity):
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
	

player = Character(hp=15, ac=15, attack_bonus=4, damage=6, dexterity=16)
enemies = []
enemies += [Character(hp=7, ac=13, attack_bonus=3, damage=4, dexterity=12)]
enemies += [Character(hp=7, ac=13, attack_bonus=3, damage=4, dexterity=12)]
enemies += [Character(hp=7, ac=13, attack_bonus=3, damage=4, dexterity=12)]
enemies += [Character(hp=7, ac=13, attack_bonus=3, damage=4, dexterity=12)]

player_wins = 0
leftover_hp = 0
max_final_player_hp = 0
num_simulations = 100

for _ in range(num_simulations):
	for enemy in enemies:
		player.initiative = random.randint(1, 20) + player.dexterity
		enemy.initiative = random.randint(1, 20) + enemy.dexterity
		initiative_order = [player, enemy]
		initiative_order.sort(key=lambda x: x.initiative, reverse=True)
		while player.is_alive() and enemy.is_alive():
			for character in initiative_order:
				if character.is_alive():
					if character == player:
						character.attack(enemy)
					else:
						character.attack(player)

	if player.is_alive():
		leftover_hp += player.hp
		if player.hp > max_final_player_hp:
			max_final_player_hp = player.hp
		player_wins += 1

	# Reset characters for the next battle
	player.hp = player.original_hp
	for enemy in enemies:
		enemy.hp = enemy.original_hp

# Calculate win percentage
win_percentage = (player_wins / num_simulations) * 100
average_final_player_hp = leftover_hp / num_simulations

print(f"{win_percentage=}")
print(f"{average_final_player_hp=}")
print(f"{max_final_player_hp=}")
