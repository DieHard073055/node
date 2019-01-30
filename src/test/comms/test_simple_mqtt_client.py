"""Test for Simple Mqtt Client"""

__author__ = 'Eshan Shafeeq'

import comms
import unittest
import unittest.mock

class Client(object):
    def __init__(self, device_endpoint):
        print('mocked Client : ' + device_endpoint)

    def connect(self):
        print('mocked connect')

    def subscribe(self):
        print('mocked subscribe')

class TestSimpleMqttClient(unittest.TestCase):

    def setUp(self):
        pass

    @unittest.mock.patch('comms.mqtt.simple_mqtt_client.Client')
    def testPublish_normalStringData(self, sc):
        sc.side_effect = Client
        smc = comms.mqtt.simple_mqtt_client.SimpleMqttClient('c579d283-417e-51c5-83ed-be5fc5cbcf54')



    @unittest.mock.patch('comms.mqtt.simple_mqtt_client.Client')
    def testPublish_noHostSetup(self, mqtt_client):
        pass

    @unittest.mock.patch('comms.mqtt.simple_mqtt_client.Client')
    def testPublish_dataNone(self, mqtt_client):
        pass


if __name__ == '__main__':
    unittest.main()
