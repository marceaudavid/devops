import pickle
import socket

# Create a socket (SOCK_STREAM means a TCP socket)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((socket.gethostname(), 5000))

data = b""
while True:
    packet = server_socket.recv(4096)
    if not packet: break
    data += packet

data_arr = pickle.loads(data)
