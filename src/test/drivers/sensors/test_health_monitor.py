""" Tests for the health_monitor """

__author__ = 'Eshan Shafeeq'

import unittest
import json
from test import saved_configs
from drivers.sensors import health_monitor


class TestHealthMonitor(unittest.TestCase):

    def setUp(self):
        self.config = saved_configs.get_config()['drivers'][0]['params']
        self.hm = health_monitor.HealthMonitor(self.config)


    def test_read_cpu_temp(self):
        for param in self.config:
            if param['type'] is 'shell':
                print(param)


if __name__ == '__main__':
    unittest.main()
