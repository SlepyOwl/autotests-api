import socket


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost',12345)
    server_socket.bind(server_address)

    server_socket.listen(5)
    print("Сервер запущен и ждёт подключений . . .")

    while True:
        clinet_socket, client_address = server_socket.accept()
        print(f"Подключение от {client_address}")

        data = clinet_socket.recv(1024).decode()
        print(f"Получено сообщение: {data}")

        response = f"Сервер получил: {data}"
        clinet_socket.send(response.encode())

        clinet_socket.close()


if __name__ == '__main__':
    server()