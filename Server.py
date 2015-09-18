import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_name = 'localhost'
size = 1024
server_port = input("Masukkan Port: ")
server_socket.bind((server_name, server_port))
server_socket.listen(50)

while True:
    print 'Menunggu koneksi pada port: ', server_port
    client, client_address = server_socket.accept()
    print 'Menerima koneksi dari', client_address
    while True:
        try:
            pesan = client.recv(size)
            if not pesan: break
            print pesan
        except:
            client.close()

server_socket.close()
