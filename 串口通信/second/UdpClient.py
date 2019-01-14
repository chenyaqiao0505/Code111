import socket
import time

BUFSIZE = 1024
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def buttonclick():
    while True:
        msg = input("输入相关信息： ").strip()
        ip_port = ('127.0.0.1', 7000)
        try:
            client.sendto(msg.encode('utf-8'), ip_port)
            data, server_addr = client.recvfrom(BUFSIZE)

        except OSError:
            print('网络接口有异常，请检查接口是否正确')

        except ConnectionResetError:
            print('端口未打开！~')

        except UnboundLocalError :
            print('请检查网络接口是否正确~！')

        finally:
            time.sleep(3)
            buttonclick()

        print('客户端recvfrom ', data, server_addr)
    client.close()

def valuenone(data):
    if data == None:
        print('请过三秒再尝试~！')
        time.sleep(3)


if __name__ == '__main__':
    buttonclick()