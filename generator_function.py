import json
import random

file_name = "dane.json"


def generate_male_name():
    return generate_name(False)


def generate_female_name():
    return generate_name(True)


def generate_unisex_last_name():
    pass


def generate_male_last_name():
    pass


def generate_address():
    return generate_street() + generate_city()


def generate_street():
    pass


def generate_city():
    pass


def generate_female_person():
    return json.dumps({"first_name": generate_female_name(), "last_name": generate_unisex_last_name(), "address": generate_address()})


def generate_name(sex):
    if sex:
        return random_value_for_key("first_names_female")
    else:
        return random_value_for_key("first_names_male")


def random_value_for_key(key_name):
    with open(file_name) as f:
        data = json.load(f)
        value = data[key_name]
        return random.choice(list(value))


def write_Json_to_file(json):
    pass




