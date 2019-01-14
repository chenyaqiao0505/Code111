import paho.mqtt.client as mqtt
import time

HOST = "127.0.0.1"
PORT = 8222

def client_loop():
    # client_id = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    client_id = 'client002'

    client = mqtt.Client(client_id)    # ClientId不能重复，所以使用当前时间
    client.username_pw_set("username002", "psw002")  # 必须设置，否则会返回「Connected with result code 4」
    print("11111111")
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 6)
    client.loop_forever()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # client.subscribe("test")
    for m in range(10000):
        sub = "zhy" + str(m)
        client.subscribe(sub)
    print("订阅完毕 ")



def on_message(client, userdata, msg):
    print('qqq')
    print(msg.topic+" "+msg.payload.decode("utf-8"))

if __name__ == '__main__':
    client_loop()
