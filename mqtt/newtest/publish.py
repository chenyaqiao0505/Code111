# encoding: utf-8

import paho.mqtt.client as mqtt

HOST = "127.0.0.1"
PORT = 61613


def test():
    client = mqtt.Client()
    client.connect(HOST, PORT, 60)
    for i in range(1000):
        client.publish("chat %d"%i, "hello " , 2)  # 发布一个主题为'chat',内容为‘hello liefyuan’的信息
        print('chat publish succeed ~! %d'%i)
    client.loop_forever()


if __name__ == '__main__':
    test()
