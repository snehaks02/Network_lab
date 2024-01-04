import socket
server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 8081)  
server_socket.bind(server_address)
server_socket.listen(1)
client_socket,client_address=server_socket.accept()
print("Connected to Client {}" .format(client_address))

while true:
	data=client_socket.recv(1024).decode('utf-8')
	if data=="hi":
		response= "HELLO"
	elif data=="exit":
		response="closed connection"
		break;
	else:
		response="Data Unavailable"
		
	client_socket.sendall(response.encode('utf-8'))
server_socket.close()


