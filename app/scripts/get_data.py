import pickle
import socket

# Create a socket (SOCK_STREAM means a TCP socket)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((socket.gethostname(), 5000))

while True:
    received = server_socket.recv(16)
    dict = pickle.loads(received)
    print(dict)
