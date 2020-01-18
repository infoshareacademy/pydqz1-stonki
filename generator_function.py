import json
import random
import string


file_name = "dane.json"


def generate_male_name():
    return generate_name(False)


def generate_female_name():
    return generate_name(True)


def generate_unisex_last_name():
    with open(file_name) as f:
        data = json.load(f)
        value = data["unisex_last_names"]
        return random.choice(list(value))


def generate_male_last_name():
    with open(file_name) as f:
        data = json.load(f)
        value = data["male_last_names"]
        return random.choice(list(value))


def generate_address():
    return generate_street() + " "+ generate_city()


def generate_street():
    with open(file_name) as f:
        data = json.load(f)
        value = data["streets"]
        return random.choice(list(value))


def generate_city():
    with open(file_name) as f:
        data = json.load(f)
        value = data["cities"]
        return random.choice(list(value))


def generate_female_person():
    return json.dumps({"first_name": generate_female_name(), "last_name": generate_unisex_last_name(), "address": generate_address()})


def generate_nick():
    return letters_generator() + numbers_generator()


def letters_generator(chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for y in range(6))


def numbers_generator(chars=string.digits):
    return ''.join(random.choice(chars) for x in range(2))


def generate_name(sex):
    if sex:
        return random_value_for_key("first_names_female")
    else:
        return random_value_for_key("first_names_male")


def generate_domain():
    with open(file_name) as f:
        data = json.load(f)
        value = data["domains"]
        return random.choice(list(value))


def generate_random_emails():
    for i in range(1):
        return generate_unisex_last_name() + "@" + generate_domain()


def random_value_for_key(key_name):
    with open(file_name) as f:
        data = json.load(f)
        value = data[key_name]
        return random.choice(list(value))


def write_Json_to_file(json):
    pass
    # with open("generate_data.json", "w") as new_data:
    #     json.dump(....., new_data)
    # print("Zapisano dane.")




