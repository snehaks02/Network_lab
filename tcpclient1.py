import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('127.0.0.1',8000)
client_socket.connect(server_address)
while True:
	message=input("enter the msg:")
	client_socket.send(message.encode())
	
