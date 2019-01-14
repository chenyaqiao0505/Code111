from socket import *
from time import ctime


HOST = ''
PORT = 50505
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)


while True:
    print('等待链接...')
    tcpCliSock,ADDR = tcpSerSock.accept()
    print('连接来自:%s',ADDR)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
            tcpCliSock.send(' %s' % data)

    tcpCliSock.close()
    tcpSerSock.close()
