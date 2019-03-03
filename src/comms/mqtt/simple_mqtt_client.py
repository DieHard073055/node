""" Simple MQTT Client """

__author__ = 'Eshan Shafeeq'

from paho.mqtt.client import Client

class SimpleMqttClient(Client):

    def __init__(self, device_endpoint, host="localhost", port=1883, sub_list=[], timeout=60):
        super().__init__(device_endpoint)
        self.device_endpoint = device_endpoint
        self.host = host
        self.port = port
        self.timeout = timeout
        if sub_list == []:
            sub_list.append('/'+device_endpoint + '/*')

        self.sub_list = sub_list
        self.count = 0

    def on_connect(self, client, obj, flag, rc):
        print('connected : ' + str(client))

    def on_message(self, client, obj, msg):
        #print('message : ' + str(msg.payload) + ' from topic : ' + msg.topic)
        print(str(self.count) + ' == ' + str(msg.payload))
        self.count+=1

    def on_publish(self, client, obj, msg):
        print('puublish : ' + msg)

    def on_subscribe(self, client, obj, mid, granted_pos):
        print('subscribed  : ' + str(client))

    def on_log(self, client, obj, level, string):
        print('log : ' + str(string) )

    def setup(self):
        self.connect(self.host, self.port, self.timeout)
        for topic in  self.sub_list:
            self.subscribe(topic, 2)

        return_code = 0
        while return_code == 0:
            return_code = self.loop()
        return return_code
