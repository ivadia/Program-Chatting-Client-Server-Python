import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
size = 1024

server_address = raw_input("Masukkan IP Server: ")
server_port = input("Masukkan Port Server: ")
client_socket.connect((server_address, server_port))

while True:
    #data = client_socket.recv(size)
    #print data
    message = raw_input()
    if not message: break
    client_socket.send(message)
client_socket.close()
