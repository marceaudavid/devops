import pickle
import random
import socket
import threading
import string
import time
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((socket.gethostname(), os.environ["SOCKET_PORT"]))


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
    robot_number = iterate
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
        "Creation time": creation_time,
    })


def generate_json(unit_data, i):
    # Generate uniq name :
    timestamp = time.time()
    timestamp_to_string = datetime.utcfromtimestamp(
        timestamp).strftime('%Y-%m-%d %H-%M-%S')

    filename = str(int(i) + 1) + "-" + timestamp_to_string + ".json"

    # Generate json file with a unit of 10 robots :

    # server_socket.sendall(unit_data_encoded)

    # with open(os.path.join(os.path.dirname(__file__), 'yoho')), "w") as outfile:
    #     json.dump(unit_data, outfile, indent=4)

    # unit_data_json = json.load(open("json/" + filename, "w"))


def generate_a_unit(unit_number):
    for i in range(10):
        generate_a_robot((i + 1), unit_number)


def execute_generation():
    global data
    # for y in range(5): Keep it for test only
    #     generate_a_unit((y + 1))
    #     generate_json(data, y)
    generate_a_unit(os.environ["UNIT"])
    generate_json(data, os.environ["UNIT"])
    # Must empty the data, otherwise each json concatenate with the previous Unit values
    server_socket.sendall(pickle.dumps(data))
    data = {'robots': []}
    threading.Timer(60.0, execute_generation).start()


execute_generation()
