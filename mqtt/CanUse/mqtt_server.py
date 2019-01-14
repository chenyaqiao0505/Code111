# import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time

HOST = "127.0.0.1"
PORT = 8222

def cycle():
    # client_id = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    # for i in range(20000):
    client_id = 'client001'
    pub = "zhy"
        #将一条消息发布给代理，然后彻底断开连接
    publish.single(pub, '这是发布者', qos=1, hostname=HOST, port=PORT,
            client_id=client_id, auth={'username': "username001", 'password': "psw001"})

if __name__ == '__main__':
    cycle()
