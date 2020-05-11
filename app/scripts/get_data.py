import json
import pickle
import socket

# Create a socket (SOCK_STREAM means a TCP socket)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((socket.gethostname(), 5000))

data_dict = ""
while True:
    data = server_socket.recv(195000)
    data_dict = pickle.loads(data)

    # print(data_dict.get('robots', {}))
    for y in range(10):
        print(data_dict.get("robots", {})[y].get("Robot number")) # Stock this in a previous variable and repeat this for each value of robot to store it in database

    if data_dict != "":
        data_dict = ""
