from socket import *
# 10.0.0.156 Mio
# 192.168.0.77 L
# Testeo
# Lexi Test
serverName = '10.250.145.79'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print('\n Connect to:', '10.192.254.101,4000')

while True:
	sentence = input('Input your guess number is:')
	clientSocket.send(sentence.encode())
	modifiedSentence = clientSocket.recv(1024).decode()
	print(modifiedSentence)
	if modifiedSentence == ("correct"):
		break
clientSocket.close()