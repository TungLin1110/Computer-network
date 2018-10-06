from socket import *
serverName = 'localhost'	# or 'hostname'
serverPort = 12000
clientSocket = socket(socket.AF_INET, socket.SOCK_DGRAM)
message = raw_input('Input lowercase sentence: ')
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
# print("Received message from %s port %s"%(serverAddress[0],serverAddress[1]))
print(modifiedMessage.decode())
clientSocket.close()
