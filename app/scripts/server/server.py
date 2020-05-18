import os
import pickle
import socket
import time

import mysql.connector

# Create a socket (SOCK_STREAM means a TCP socket)

from dotenv import load_dotenv

time.sleep(15)

load_dotenv()

# Create a socket (SOCK_STREAM means a TCP socket)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind((socket.gethostname(), 5000))
except socket.error:
    print("The socket can't bind to the chosen address")

cnx = mysql.connector.connect(user=os.environ['MYSQL_USER'], password=os.environ['MYSQL_PASSWORD'],
                              host=os.environ['MYSQL_HOST'], database=os.environ['MYSQL_DATABASE'])

cursor = cnx.cursor(buffered=True)


def set_robot_data(y):
    unit_number = data_dict.get("robots", {})[y].get("Unit number")
    robot_number = data_dict.get("robots", {})[y].get("Robot number")
    robot_type = data_dict.get("robots", {})[y].get("Robot type")
    tank_temperature = data_dict.get("robots", {})[y].get("Tank temperature (Celsius)")
    external_temperature = data_dict.get("robots", {})[y].get("External temperature (Celsius)")
    weight_of_milk_in_tank = data_dict.get("robots", {})[y].get("Weight of milk in tank (Kg)")
    ph_measure = data_dict.get("robots", {})[y].get("pH measure")
    k_measure = data_dict.get("robots", {})[y].get("K+ measure (mg/litre)")
    nacl_concentration = data_dict.get("robots", {})[y].get("NaCL concentration (g/litre)")
    salmonella_bacterium_level = data_dict.get("robots", {})[y].get("Salmonella bacterium level (ppm)")
    e_coli_bacterium_level = data_dict.get("robots", {})[y].get("E-coli bacterium level (ppm)")
    listeria_bacterium_level = data_dict.get("robots", {})[y].get("Listeria bacterium level (ppm)")
    creation_time = data_dict.get("robots", {})[y].get("Creation time")

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

    return data_robot


data_dict = ""

while True:
    print("Server is ready :")
    server_socket.listen(5)
    clientsocket, address = server_socket.accept()

    data = clientsocket.recv(195000)
    data_dict = pickle.loads(data)

    for y in range(0, 10):
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

        data_robot = set_robot_data(y)
        set_robot_data(y)

        cursor.execute(add_robot, data_robot)
        cnx.commit()

    if data_dict != "":
        data_dict = ""
