# import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time

HOST = "127.0.0.1"
PORT = 8222


# def on_connect(client, userdata, flags, rc):
#     print("Connected with result code "+str(rc))
#     client.subscribe("test")

#     # for m in range(100):
#     #     sub = "test" + str(m)
#     #     client.subscribe(sub)


# def on_message(client, userdata, msg):
#     print(msg.topic+" "+msg.payload.decode("utf-8"))


def cycle():
    client_id = 'client001'
    # publish.single("test", "你好 MQTT", qos=1, hostname=HOST, port=PORT,
    #                       client_id=client_id, auth={'username': "admin", 'password': "password"})

    for i in range(10000):
        pub = "zhy" + str(i)
        publish.single(pub, '这是{}个发布者'.format(i), qos=1, hostname=HOST, port=PORT,
            client_id=client_id, auth={'username': "username001", 'password': "psw001"})
        print(i)
        time.sleep(0.1)


if __name__ == '__main__':

    cycle()
