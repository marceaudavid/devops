import json
import random
import string
import time
from datetime import datetime

default_unit_number = 1  # replace this with database value to swap to unit 2, 3... and implement change every 10 robot


def get_unit_number(number):
    if number <= 10:
        number = 1
        return number
    else:
        number += 1
        return number


def get_robot_type():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(12))


def get_tank_temperature():
    return round(random.uniform(2.5, 4.1), 1)


def get_external_temperature():
    return round(random.uniform(9, 14.1), 1)


def get_weight_of_milk_in_tank():
    return round(random.uniform(3512, 4608))


def get_ph_measure():
    return round(random.uniform(6.8, 7.3), 1)


def get_k_measure():
    return round(random.uniform(35, 48))


def get_naci_concentration():
    return round(random.uniform(1, 1.71), 2)


def get_salmonella_bacterium_level():
    return round(random.uniform(17, 38))


def get_e_coli_bacterium_level():
    return round(random.uniform(35, 50))


def get_listeria_bacterium_level():
    return round(random.uniform(28, 55))


data = {'robots': []}


def generate_a_robot(previous_weight_of_milk, iterate):
    new_weight_of_milk = get_weight_of_milk_in_tank()
    if iterate == 0:
        tank_weight_difference = 0
    else:
        tank_weight_difference = new_weight_of_milk - previous_weight_of_milk

    data['robots'].append({
        "Unit number": get_unit_number(default_unit_number),
        "Robot number": iterate + 1,
        "Robot type": get_robot_type(),
        "Tank temperature (Celsius)": get_tank_temperature(),
        "External temperature (Celsius)": get_external_temperature(),
        "Weight of milk in tank (Kg)": new_weight_of_milk,
        "Weight ok milk difference (Kg)": tank_weight_difference,
        "pH measure": get_ph_measure(),
        "K+ measure (mg/litre)": get_k_measure(),
        "NaCL concentration (g/litre)": get_naci_concentration(),
        "Salmonella bacterium level (ppm)": get_salmonella_bacterium_level(),
        "E-coli bacterium level (ppm)": get_e_coli_bacterium_level(),
        "Listeria bacterium level (ppm)": get_listeria_bacterium_level(),
    })


def generate_json(unit_data):
    # Generate uniq name :

    timestamp = time.time()
    timestamp_to_string = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H-%M-%S')

    filename = str(get_unit_number(default_unit_number)) + "-" + timestamp_to_string + ".json"

    # Generate json file with a unit of 10 robots :

    with open(filename, "w") as outfile:
        json.dump(unit_data, outfile, indent=4)


def generate_a_unit():
    for i in range(10):
        get_new_weight_of_milk = get_weight_of_milk_in_tank()
        generate_a_robot(get_new_weight_of_milk, i)


generate_a_unit()
generate_json(data)
