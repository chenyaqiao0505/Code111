# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import time

MQTTHOST = "127.0.0.1"
MQTTPORT = 61613
mqttClient = mqtt.Client()


# 连接MQTT服务器
def on_mqtt_connect():
    mqttClient.connect(MQTTHOST, MQTTPORT, 60)
    mqttClient.loop_start()


# publish 消息
def on_publish(topic, payload, qos):
    mqttClient.publish(topic, payload, qos)
    print(topic,payload)


# 消息处理函数
def on_message_come(lient, userdata, msg):
    print(msg.topic + " " + ":" + str(msg.payload))


# subscribe 消息
def on_subscribe():
    mqttClient.subscribe("/server", 1)
    mqttClient.on_message = on_message_come  # 消息到来处理函数
    print(on_message_come)


def main():
    on_mqtt_connect()
    for i in range(10000):
        on_publish("test server", "Hello Python!", 1)
        on_subscribe()
        time.sleep(0.3)


if __name__ == '__main__':
    main()
