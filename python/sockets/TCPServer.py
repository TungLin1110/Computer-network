from socket import *
serverPort = 25531
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print("Welcome! I'm A1035531 from Taiwan.")
while 1:
	connectionSocket, addr = serverSocket.accept()
	print(connectionSocket.getpeername())
	sentence = connectionSocket.recv(1024)
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence)
	connectionSocket.close()
