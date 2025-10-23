# import socket
#
# def server():
#      server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
#      server_address = ("localhost", 12345)
#      server_socket.bind(server_address)
#
#      server_socket.listen(5)
#      print(f"Статус сервера: ожидает подключения.")
#
#      while True:
#          client_socket, client_address = server_socket.accept()
#          print(f"Статус сервера: клиент подключился с адрес - {client_address}")
#
#          data = client_socket.recv(1024).decode()
#          print(f"Статус серера: сервер получил сообщение - {data}")
#
#          response = f"Статус клиента: сервер отправил сообщение - {data}"
#          client_socket.send(response.encode())
#
#          client_socket.close()
#
# if __name__ == "__main__":
#     server()