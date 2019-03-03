import paho.mqtt.publish as publish
import datetime
import json
import time


packet ="mqtt message from message tester : {}"

for i in range(1000):
    message = json.dumps({"message":packet.format(i)})
    publish.single('/4f5b7d88-c984-5be2-b246-201e543ba7b2/something', str(i), hostname='localhost', port=1883, qos=2)
    print('sent message : ' + message)
    time.sleep(0.1)

