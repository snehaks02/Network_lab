import socket
server_address=('127.0.0.1',8000)
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(server_address)

while True:
	message=input("enter the message:")
	client_socket.send(message.encode())
	
	if(message=="bye"):
		break
		
	data=client_socket.recv(1024)
	print(f"server:{data.decode()}")
	
client_socket.close()
