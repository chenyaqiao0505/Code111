# import paho.mqtt.client as mqtt
import paho.mqtt.client as mqtt
import json
mqttc = mqtt.Client()
mqttc.connect('127.0.0.1', port=61680)
msg = {
    'pin': 17,
    'value': 10
}
msg = json.dumps(msg)

print(mqttc.publish('baisong', payload=msg))
mqttc.loop_forever(2)