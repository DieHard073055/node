"""Script to send test messages to mqtt client"""

__author__ = 'Eshan Shafeeq'

import paho.mqtt.publish as publish
import unittest

class TestMqttClientRecieveMessage(unittest.TestCase):
    def setUp(self):
        self.device_endpoint = '4f5b7d88-c984-5be2-b246-201e543ba7b2/stuff'

    def testSendingMessage(self):
        publish.single(self.device_endpoint, 'lol', hostname='localhost', port=1883)


if __name__ == '__main__':
    unittest.main()
