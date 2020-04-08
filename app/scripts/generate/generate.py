import json
import random
import string
import time
from datetime import datetime

default_unit_number = 1  # replace this with database value to swap to unit 2, 3... and implement change every 10 robot


def generate_unit_number(number):
    if number <= 10:
        number = 1
        return number
    else:
        number += 1
        return number


def generate_robot_type():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(12))


def generate_tank_temperature():
    return round(random.uniform(2.5, 4.1), 1)


def external_temperature():
    return round(random.uniform(9, 14.1), 1)


def generate_weight_of_milk_in_tank():
    return round(random.uniform(3512, 4607))


data = {'robots': []}


def generate_a_unit(previous_weight_of_milk, iterate):
    new_weight_of_milk = generate_weight_of_milk_in_tank()
    if iterate == 0:
        tank_weight_difference = 0
    else:
        tank_weight_difference = new_weight_of_milk - previous_weight_of_milk

    print("previous weight of milk :", previous_weight_of_milk)
    print("tank weight difference :", tank_weight_difference)
    data['robots'].append({
        "Unit number": generate_unit_number(default_unit_number),
        "Robot number": i + 1,
        "Robot type": generate_robot_type(),
        "Tank temperature (Celsius)": generate_tank_temperature(),
        "External temperature (Celsius)": external_temperature(),
        "Weight of milk in tank (Kg)": new_weight_of_milk,
        "Weight ok milk difference (Kg)": tank_weight_difference,
    })


def generate_json(unit_data):
    # Generate uniq name :

    timestamp = time.time()
    timestamp_to_string = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H-%M-%S')

    filename = str(generate_unit_number(default_unit_number)) + "-" + timestamp_to_string + ".json"

    # Generate json file with a unit of 10 robots :

    with open(filename, "w") as outfile:
        json.dump(unit_data, outfile, indent=4)


for i in range(10):
    generate_new_weight_of_milk = generate_weight_of_milk_in_tank()
    generate_a_unit(generate_new_weight_of_milk, i)

generate_json(data)
