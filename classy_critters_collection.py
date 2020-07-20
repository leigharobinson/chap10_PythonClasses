# Critters, Croquettes Petting Zoo and Tapas Bar
# Current Animals
from datetime import date


class Llama:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()


miss_fuzz = Llama()
miss_fuzz.name = "Miss Fuzz"
miss_fuzz.species = "domestic llama"
for prop, value in miss_fuzz.__dict__.items():
    print(f'{prop}:\n{value}\n')
