from socket import *
import time

class udpclient:
    def __init__(self):
        self.buffer_size = 1024
        self.udpClientSocket = socket(AF_INET, SOCK_DGRAM)
        self.udpClientSocket.settimeout(1)
        

    def control(self,msg, status):
        ip_port = ('192.168.1.253', 5000)
        self.udpClientSocket.sendto(msg, ip_port)
        time.sleep(0.3)
        if status:            
            try:
                data,server_addr = self.udpClientSocket.recvfrom(self.buffer_size)
                #print(data)
                return data
            except TimeoutError:
                print('请求超时~！')
            except OSError:
                print('网络接口有异常，请检查接口是否正确')

            except ConnectionResetError:
                print('端口未打开！~')

            except UnboundLocalError:
                print('请检查网络接口是否正确~！')
                
    def __del__(self):
        self.udpClientSocket.close()
    

     

