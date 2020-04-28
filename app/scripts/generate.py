import json
import pickle
import random
import socket
import threading
import string
import time
import os
import mysql.connector
from datetime import datetime
from dotenv import load_dotenv

# replace this with database value to swap to unit 2, 3... and implement change every 10 robot
default_unit_number = 1

load_dotenv()

cnx = mysql.connector.connect(user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASSWORD'],
                              host=os.environ['MYSQL_HOST'], database=os.environ['MYSQL_DATABASE'])

cursor = cnx.cursor(buffered=True)

# Create a socket (SOCK_STREAM means a TCP socket)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), 5000))
# server_socket.setblocking(False)
server_socket.listen(5)
clientsocket, address = server_socket.accept()


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


def get_nacl_concentration():
    return round(random.uniform(1, 1.71), 2)


def get_salmonella_bacterium_level():
    return round(random.uniform(17, 38))


def get_e_coli_bacterium_level():
    return round(random.uniform(35, 50))


def get_listeria_bacterium_level():
    return round(random.uniform(28, 55))


def get_time():
    return time.strftime('%Y-%m-%d %H:%M:%S')


data = {'robots': []}


def generate_a_robot(iterate, unit_number):
    weight_of_milk_in_tank = get_weight_of_milk_in_tank()
    robot_number = iterate + 1
    unit_number = unit_number
    robot_type = get_robot_type()
    tank_temperature = get_tank_temperature()
    external_temperature = get_external_temperature()
    ph_measure = get_ph_measure()
    k_measure = get_k_measure()
    nacl_concentration = get_nacl_concentration()
    salmonella_bacterium_level = get_salmonella_bacterium_level()
    e_coli_bacterium_level = get_e_coli_bacterium_level()
    listeria_bacterium_level = get_listeria_bacterium_level()
    creation_time = get_time()

    data['robots'].append({
        "Unit number": unit_number,
        "Robot number": robot_number,
        "Robot type": robot_type,
        "Tank temperature (Celsius)": tank_temperature,
        "External temperature (Celsius)": external_temperature,
        "Weight of milk in tank (Kg)": weight_of_milk_in_tank,
        "pH measure": ph_measure,
        "K+ measure (mg/litre)": k_measure,
        "NaCL concentration (g/litre)": nacl_concentration,
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
        "ph_measure": ph_measure,
        "k_measure": k_measure,
        "nacl_concentration": nacl_concentration,
        "salmonella_bacterium_level": salmonella_bacterium_level,
        "e_coli_bacterium_level": e_coli_bacterium_level,
        "listeria_bacterium_level": listeria_bacterium_level,
        "creation_time": creation_time
    }

    add_robot = ("INSERT INTO robots "
                 "(unit_number,"
                 "robot_number,"
                 "robot_type,"
                 "tank_temperature,"
                 "external_temperature,"
                 "weight_of_milk_in_tank,"
                 "ph_measure,"
                 "k_measure,"
                 "nacl_concentration,"
                 "salmonella_bacterium_level,"
                 "e_coli_bacterium_level,"
                 "listeria_bacterium_level,"
                 "creation_time)"
                 "VALUES ("
                 "%(unit_number)s,"
                 "%(robot_number)s,"
                 "%(robot_type)s,"
                 "%(tank_temperature)s,"
                 "%(external_temperature)s,"
                 "%(weight_of_milk_in_tank)s,"
                 "%(ph_measure)s,"
                 "%(k_measure)s,"
                 "%(nacl_concentration)s,"
                 "%(salmonella_bacterium_level)s,"
                 "%(e_coli_bacterium_level)s,"
                 "%(listeria_bacterium_level)s,"
                 "%(creation_time)s"
                 ")"
                 )
    cursor.execute(add_robot, data_robot)
    cnx.commit()


def generate_json(unit_data, i):
    # Generate uniq name :
    timestamp = time.time()
    timestamp_to_string = datetime.utcfromtimestamp(
        timestamp).strftime('%Y-%m-%d %H-%M-%S')

    filename = str(int(i) + 1) + "-" + timestamp_to_string + ".json"

    # Generate json file with a unit of 10 robots :
    while True:
        # unit_data_encoded = json.dumps(unit_data).encode('utf-8')
        # server_socket.sendall(unit_data_encoded)

        with open("json/" + filename, "w") as outfile:
            json.dump(unit_data, outfile, indent=4)

        unit_data_json = json.load(open("json/" + filename, "w"))
        # unit_data_json = ['foo', {'bar': ('baz', None, 1.0, 2)}]
        print(unit_data_json)
        clientsocket.send(pickle.dumps(unit_data_json))


def generate_a_unit(unit_number):
    for i in range(10):
        generate_a_robot(i, unit_number)


def execute_generation():
    global data
    for y in range(5):
        generate_a_unit(y + 1)
        generate_json(data, y)
    # generate_a_unit(os.environ["UNIT"]) TODO: Remetttre comme ça à la fin après les tests
    # generate_json(data, os.environ["UNIT"]) TODO: Remetttre comme ça à la fin après les tests
    # Must empty the data, otherwise each json concatenate with the previous Unit values
    data = {'robots': []}
    threading.Timer(60.0, execute_generation).start()


execute_generation()
