import socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('127.0.0.1',8000)

server_socket.bind(server_address)
server_socket.listen(5)
print(f"server is listening")

client_socket,client_address=server_socket.accept()
print(f"accepted connection from {client_address}")

while True:
	data=client_socket.recv(1024)
	print(f"client:{data.decode()}")
	
	if(data=="bye"):
		break
		
	message=input("server:")
	client_socket.send(message.encode())
	
client_socekt.close()
server_socket.close()
