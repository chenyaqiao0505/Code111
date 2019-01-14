# coding=utf-8
import paho.mqtt.client as mqtt
import json
#
def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))
    client.subscribe('baisong')


def on_message(client, userdata, msg):
    print (msg.topic + ' ' + str(msg.payload))
    print (json.loads(msg.payload))

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect('127.0.0.1', port=61680)
        client.loop_forever()
    except KeyboardInterrupt:
        client.disconnect()