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
        read_cpu_temp_command = {'key': 'cpu_temp_0', 'type': 'shell', 'command': ['cat', '/sys/class/thermal/thermal_zone0/temp']}
        key = read_cpu_temp_command['key']
        command = read_cpu_temp_command['command']
        cpu_temp = self.hm._exec_shell(key, command)
        actual_cpu_temp = 0
        with open(command[1], 'r') as cpu_temp_file:
            actual_cpu_temp = {key:cpu_temp_file.read()}
        self.assertEqual(cpu_temp, actual_cpu_temp)



if __name__ == '__main__':
    unittest.main()
