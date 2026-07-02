import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


server_addres = ('localhost', 12345)
client_socket.connect(server_addres)

message = "Привет, Сервер!"
client_socket.send(message.encode())

response = client_socket.recv(1024).decode()
print(response)

client_socket.close