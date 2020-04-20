import json
import random
import string
import time
import mysql.connector
from datetime import datetime

default_unit_number = 1  # replace this with database value to swap to unit 2, 3... and implement change every 10 robot

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='devops')

cursor = cnx.cursor()


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


def generate_a_robot(iterate):
    weight_of_milk_in_tank = get_weight_of_milk_in_tank()

    if iterate == 0:
        weight_of_milk_difference = 0
    else:
        # Faire un select :récupérer weight_of_milk_in_tank du robot précédent et remplacer -1 par cette value
        weight_of_milk_difference = weight_of_milk_in_tank - 1

    unit_number = get_unit_number(default_unit_number)
    robot_number = iterate + 1
    robot_type = get_robot_type()
    tank_temperature = get_tank_temperature()
    external_temperature = get_external_temperature()
    ph_measure = get_ph_measure()
    k_measure = get_k_measure()
    naci_concentration = get_naci_concentration()
    salmonella_bacterium_level = get_salmonella_bacterium_level()
    e_coli_bacterium_level = get_e_coli_bacterium_level()
    listeria_bacterium_level = get_listeria_bacterium_level()

    data['robots'].append({
        "Unit number": unit_number,
        "Robot number": robot_number,
        "Robot type": robot_type,
        "Tank temperature (Celsius)": tank_temperature,
        "External temperature (Celsius)": external_temperature,
        "Weight of milk in tank (Kg)": weight_of_milk_in_tank,
        "Weight ok milk difference (Kg)": weight_of_milk_difference,
        "pH measure": ph_measure,
        "K+ measure (mg/litre)": k_measure,
        "NaCL concentration (g/litre)": naci_concentration,
        "Salmonella bacterium level (ppm)": salmonella_bacterium_level,
        "E-coli bacterium level (ppm)": e_coli_bacterium_level,
        "Listeria bacterium level (ppm)": listeria_bacterium_level,
    })

    data_robot = {
        "unit_number": unit_number,
        "robot_number": robot_number,
        "robot_type": robot_type,
        "tank_temperature": tank_temperature,
        "external_temperature": external_temperature,
        "weight_of_milk_in_tank": weight_of_milk_in_tank,
        "weight_of_milk_difference": weight_of_milk_difference,
        "ph_measure": ph_measure,
        "k_measure": k_measure,
        "naci_concentration": naci_concentration,
        "salmonella_bacterium_level": salmonella_bacterium_level,
        "e_coli_bacterium_level": e_coli_bacterium_level,
        "listeria_bacterium_level": listeria_bacterium_level,
    }

    add_robot = ("INSERT INTO robots "
                    "(unit_number,"
                    "robot_number,"
                    "robot_type,"
                    "tank_temperature,"
                    "external_temperature,"
                    "weight_of_milk_in_tank,"
                    "weight_of_milk_difference,"
                    "ph_measure,"
                    "k_measure,"
                    "naci_concentration,"
                    "salmonella_bacterium_level,"
                    "e_coli_bacterium_level) "
                    "VALUES ("
                    "%(unit_number)s,"
                    "%(robot_number)s,"
                    "%(robot_type)s,"
                    "%(tank_temperature)s,"
                    "%(external_temperature)s,"
                    "%(weight_of_milk_in_tank)s,"
                    "%(weight_of_milk_difference)s,"
                    "%(ph_measure)s,"
                    "%(k_measure)s,"
                    "%(naci_concentration)s,"
                    "%(salmonella_bacterium_level)s,"
                    "%(e_coli_bacterium_level)s"
                    ")"
                 )
    cursor.execute(add_robot, data_robot)
    cnx.commit()


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
        generate_a_robot(i)


generate_a_unit()
generate_json(data)
cursor.close()
cnx.close()
