# import the python datetime module to help us create a timestamp
from datetime import date

# 1


class Llama:

    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True

# 2


class Donkey:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
# 3


class Goat:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
# 4


class Pony:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
# 5


class Turkey:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.walking = True
# 6


class Copperhead:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
# 7


class Rat_Snake:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
# 8


class Northern_Water_Snake:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
# 9


class King_Snake:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True

# 10


class Timber_Rattlesnake:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
# 11


class Mallard:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

# 12


class Goldfish:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
# 13


class Yellow_Bellied_Slider:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
# 14


class Brook_Trout:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True

# 15


class Bluegill:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True


# 1
# miss_fuzz = Llama()
# miss_fuzz.name = "Miss Fuzz"
# miss_fuzz.species = "domestic llama"
miss_fuzz = Llama("Miss Fuzz", "domestic llama")
print("1.", miss_fuzz.name)
# 2
# mr_long_ears = Donkey()
# mr_long_ears.name = "Jack"
mr_long_ears = Donkey("Mr. Long Ears", "domestic donkey")
print("2.", mr_long_ears.name)
# 3
billy = Goat("Billy", "domestic goat")
# billy.name = "Billy"
print("3.", billy.name)
# 4
teddy = Pony("Teady", "domestic pony")
# teddy.name = "Teddy"
print("4.", teddy.name)
# 5
frank = Turkey("Frank", "domestic turkey")
# frank.name = "Frank"
print("5.", frank.name)
# 6
copper = Copperhead("Copper", "Copperhead Snake")
# copper.name = "Copper"
print("6.", copper.name)
# 7
bigBoi = Rat_Snake("Big Boy", "Rat Snake")
# bigBoi.name = "Big Boy"
print("7.", bigBoi.name)
# 8
happy = Northern_Water_Snake("Happy", "Rat Snake")
# happy.name = "Happy"
print("8.", happy.name)
# 9
the_king = King_Snake("The King", "King Snake")
# the_king.name = "The King"
print("9.", the_king.name)
# 10
ole_shakey = Timber_Rattlesnake("Shakey Graves", "Timber Rattlesnake")
# ole_shakey.name = "Shakey Graves"
print("10.", ole_shakey.name)
# 11
donald = Mallard("Donald", "Mallard")
# donald.name = "Donald"
print("11.", donald.name)
# 12
goldie = Goldfish("Goldie", "Goldfish")
# goldie.name = "Goldie"
print("12.", goldie.name)
# 13
bruce = Yellow_Bellied_Slider("Bruce", "Yellow Bellied Slider")
# brunce.name = "Bruce"
print("13.", bruce.name)
# 14
grumpy = Brook_Trout("Grumpy", "Brook Trout")
# grumpy.name = "Grumpy"
print("14.", grumpy.name)
# 15
blue_boi = Bluegill("Blue Boy", "Bluegill")
# blue_boi = "Blue Boy"
print("15.", blue_boi.name)
