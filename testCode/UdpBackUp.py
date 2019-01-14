import socket

BUFSIZE = 1024
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(5)

def control(msg, status):
    ip_port = ('192.168.1.253', 5000)
    client.sendto(msg, ip_port)
    if status:
        try:
            data,server_addr = client.recvfrom(BUFSIZE)
            #print('客户端recvfrom ', data, server_addr)
            return data
        except TimeoutError:
            print('请求超时~！')
        except OSError:
            print('网络接口有异常，请检查接口是否正确')

        except ConnectionResetError:
            print('端口未打开！~')

        except UnboundLocalError:
            print('请检查网络接口是否正确~！')

def buttonclick():
    i = 0
    DI = 0
    DO = 0
    while True:
        # The number of card
        msg = b'\xAA\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        Result = control(msg, True)
        #print('10', Result)     #输出返回数据，现在为空数据，所以无类型
        if Result!=None:
            reList = [hex(x) for x in bytes(Result)]
        # 字节串转16进制数组,再转整数
            DI = int(reList[1], 16)
            DO = int(reList[2], 16)
            print('DI:', DI, 'DO:', DO)
        # 发送控制码
        msg = b'\xAA\x03\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        Result = control(msg, False)
        print('DO Control  FF')

        # 读取DI
        msg = b'\xAA\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        Result = control(msg, True)
        reList = [hex(x) for x in bytes(Result)]
        print('DI1:', bin(int(reList[2], 16)), bin(int(reList[3], 16)), 'DI2:', bin(int(reList[4], 16)),
              bin(int(reList[5], 16)))
        #print('02——FF', Result)

        msg = b'\xAA\x03\x00\x00\x00\x00\x00\x00\x00\x00\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        Result = control(msg, False)
        print('DO Control  00')

        msg = b'\xAA\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        Result = control(msg, True)
        reList = [hex(x) for x in bytes(Result)]
        print('DI1:', bin(int(reList[2], 16)), bin(int(reList[3], 16)), 'DI2:', bin(int(reList[4], 16)),
              bin(int(reList[5], 16)))
        #print('02——00', Result)
        # 循环4次退出
        i = i + 1
        if i == 4:
            break
    client.close()
    print(DI+DO)
    return DI+DO

def checknum():
    checknum = b'\xAA\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    Result = control(checknum, True)
    print( Result)
    reList = [hex(x) for x in bytes(Result)]
    # 字节串转16进制数组,再转整数
    print('DI:', int(reList[1], 16), 'DO:', int(reList[2], 16))

if __name__ == '__main__':
    buttonclick()

