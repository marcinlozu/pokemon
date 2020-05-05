import random

class Pokemon:
	def __init__(self, name, level, poke_type, max_health, current_health):
		self.name = name
		self.level = level
		self.poke_type = poke_type
		self.max_health = max_health
		self.current_health = current_health
		self.is_knocked_out = False
		self.exp_points = 0
		

	def __repr__(self):
		return "{}, level: {}, type: {}. {} health points.".format(self.name, self.level, self.poke_type, self.current_health)

	def lose_health(self, damage):
		if damage >= self.current_health:
			self.current_health = 0
			self.is_knocked_out = True
			return print("{} takes damage! Now has {} health points. Now this pokemon is knocked out.".format(self.name, self.current_health))
		else: 
			self.current_health -= damage
			return print("{} takes damage! Now has {} health points.".format(self.name, self.current_health))

	def healing(self, healing_points):
		self.current_health += healing_points
		if self.current_health > self.max_health:
			self.current_health = self.max_health
		return print("Healing! {} now has {} health points".format(self.name, self.current_health))

	def attack(self, other, dmg_points):
		if self.is_knocked_out == True:
			return print("You cannot attack, your pokemon {} is knocked out!".format(self.name))
		if self.poke_type.lower() == "grass" and other.poke_type.lower() == "fire":
			dmg_points = dmg_points/2
		elif self.poke_type.lower() == "fire" and other.poke_type.lower() == "grass":
			dmg_points = dmg_points*2
		elif self.poke_type.lower() == "water" and other.poke_type.lower() == "fire":
			dmg_points = dmg_points*2
		elif self.poke_type.lower() == "fire" and other.poke_type.lower() == "water":
			dmg_points = dmg_points/2

		return other.lose_health(dmg_points)

class Trainer:
	potion_value = 5

	def __init__(self, name, potion_list, pokemon_list, active_pokemon):
		self.name = name
		self.potion_list = potion_list
		self.pokemon_list = pokemon_list
		self.active_pokemon = active_pokemon
		

	def __repr__(self):
		return "{} has {} as an active pokemon. All pokemon {}".format(self.name, self.active_pokemon.name, self.pokemon_list)

	def healing_pokemon(self):
		if self.active_pokemon.current_health == self.active_pokemon.max_health:
			print(f"Your {self.active_pokemon.name} has max health.")
		else:
			self.active_pokemon.healing(self.potion_value)
			

	def attack_trainer(self, other):
		self.active_pokemon.attack(other.active_pokemon, 10)

	def attack_pokemon(self, other_pokemon):
		self.active_pokemon.attack(other_pokemon, 10)

	def switch_pokemon(self, number):
		if self.pokemon_list[number].is_knocked_out == True:
			return print("You cannot switch to pokemon that is knocked out")
		else:
			self.active_pokemon = self.pokemon_list[number]
			return print("{} has changed pokemon to {}".format(self.name, self.active_pokemon.name))

class Cube:
	def left():
		print("Ok, let's go left")
		print(left_room)
		action = input(">>")
		if action.lower() in conf:
			return left_room.action()
		else:
			return start.choose_direction()

	def right():
		print("Ok, let's go right")
		print(right_room)
		action = input(">>")
		if action.lower() in conf:
			return right_room.action()
		else:
			return start.choose_direction()

	def up():
		print("Ok, let's go forward")
		print(up_room)
		action = input(">>")
		if action.lower() in conf:
			return up_room.action()
		else:
			return start.choose_direction()

	def down():
		print("Ok, let's turn around and check what's behind your back")
		print(down_room)
		action = input(">>")
		if action.lower() in conf:
			return down_room.action()
		else:
			return start.choose_direction()

def random_pokemon(rand_list):
	pokemon = rand_list[random.randint(0,len(rand_list)-1)]
	return pokemon

class Room:
	def __init__(self, pokemon):
		self.pokemon = pokemon

	def __repr__(self):
		return "In your location there is {}. Would you light to fight?".format(self.pokemon.name)
	
	def action(self):
		print("Action!")
		return ash.attack_pokemon(self.pokemon)

# TODO
# if pokemon is is_knocked_out, finish battle
# if not - continue
# print who wins the battle
# ask what's next

class Engine:
	def __repr__(self):
		print("Let's start a Pokemon game!\n You are Ash Ketchum, let's fall into Pokemon world!")
		return ash.__repr__()

	def the_game(self, direction):
		if direction == 'left':
			Cube.left()
		elif direction == 'right':
			Cube.right()
		elif direction == 'up':
			Cube.up()
		elif direction == 'down':
			Cube.down()
		else:
			print("Unknown command, please type [up], [down], [left] or [right]")
			return self.choose_direction()

	def choose_direction(self):
		print("Where to go?\n[up] move forward \n[down] go backwards \n[left] go left \n[right] go right")
		direction = input(">>").lower()
		self.the_game(direction)

conf = ['yes', 'yeah', 'yeah!', 'ja', 'ja!', 'yhy', 'mhm', 'ok']

pikachu = Pokemon('Pikachu', 2, 'Electric', 40,40)
bulbasaur = Pokemon('Bulbasaur', 1, "Grass", 30,30)
charmander = Pokemon('Charmander', 1, "Fire", 45,45)
squirtle = Pokemon('Squirtle', 2, "Water", 35,35)
psyduck = Pokemon('Psyduck', 5, "Water", 50,50)
shellder = Pokemon("Shellder", 4, "Water", 30,30)

poke_list = [pikachu, bulbasaur, charmander, squirtle, psyduck, shellder]

ash = Trainer("Ash Ketchum", [5,5,5,5], [pikachu, bulbasaur, charmander], pikachu)
# brock = Trainer("Brock", [5,5,5,5], [squirtle,psyduck,shellder], psyduck)

up_room = Room(random_pokemon(poke_list))
left_room = Room(random_pokemon(poke_list))
right_room = Room(random_pokemon(poke_list))
down_room = Room(random_pokemon(poke_list))

start = Engine()
print(start)
start.choose_direction()






