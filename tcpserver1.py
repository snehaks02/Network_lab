import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 8000)  # Corrected line
server_socket.bind(server_address)
server_socket.listen(5)

print("Server is listening")

client_socket, client_address = server_socket.accept()
print(f"Accepted connection {client_address}")

while True:
    message, address = client_socket.recvfrom(1024)
    print(message.decode())

