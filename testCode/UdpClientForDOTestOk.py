import socket
BUFSIZE = 1024
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.settimeout(5)

def control(msg,s):
    ip_port = ('192.168.1.253', 5000)
    client.sendto(msg,ip_port)
    if s:
        try:
            data,server_addr = client.recvfrom(BUFSIZE)
            print('客户端recvfrom ',data,server_addr)
            return data
        except Exception as ex:
            print(str(ex))
            if str(ex)=='timed out':
                print('tttt')
i=0
while True:
    #The number of card
    msg =b'\xAA\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    rM=control(msg,True)
    print('10',rM)
    reList=[hex(x) for x in bytes(rM)]
    #字节串转16进制数组,再转整数
    print('DI:',int(reList[1],16),'DO:',int(reList[2],16))
    #发送控制码
    msg =b'\xAA\x03\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    rM=control(msg,False)
    print('DO Control')
    #读取DI
    msg =b'\xAA\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'    
    rM=control(msg,True)
    reList=[hex(x) for x in bytes(rM)]
    print('DI1:',bin(int(reList[2],16)),bin(int(reList[3],16)),'DI2:',bin(int(reList[4],16)),bin(int(reList[5],16)))
    print('02——FF',rM)
    msg =b'\xAA\x03\x00\x00\x00\x00\x00\x00\x00\x00\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    rM=control(msg,False)
    print('DO Control')
    msg =b'\xAA\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'    
    rM=control(msg,True)
    reList=[hex(x) for x in bytes(rM)]
    print('DI1:',bin(int(reList[2],16)),bin(int(reList[3],16)),'DI2:',bin(int(reList[4],16)),bin(int(reList[5],16)))
    print('02——00',rM)
    #循环4次退出    
    i=i+1
    if i==4:
        break   
client.close()


