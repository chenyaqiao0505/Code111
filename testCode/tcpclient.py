from socket import *



HOST = 'localhost'
PORT = 9990
BUFSIZ = 1024
addr = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(addr)

while True:
    data = input('>')
    if not data:
        break
    tcpCliSock.send(bytes(data))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data)

tcpCliSock.close()
