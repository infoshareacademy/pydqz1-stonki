import json
import random
import string


class Rapdator:

    def __init__(self):
        # init function goes here

    def random_value_for_key(self, key_name):
        with open(self.file_name) as f:
            data = json.load(f)
            value = data[key_name]
            return random.choice(list(value))

    def generate_name(self, sex):
        if sex:
            return self.random_value_for_key("first_names_female")
        else:
            return self.random_value_for_key("first_names_male")





print(Rapdator.generate_male_name())
# print(Rapdator.generate_female_person())