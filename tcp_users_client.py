import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
client_socket.connect(server_address)

message_1 = f"Как дела?"

client_socket.send(message_1.encode("utf-8"))

server_response = client_socket.recv(1024).decode("utf-8")
print(server_response)

client_socket.close()