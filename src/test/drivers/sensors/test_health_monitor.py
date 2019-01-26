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

    def testResolveCommand_typeShell(self):
        request = {
            'key': 'cpu_temp_0',
            'type': 'shell',
            'command': ['cat', '/sys/class/thermal/thermal_zone0/temp']
        }
        cpu_temp = self.hm.resolve_request(request)
        print('\ncpu temp ' + str(cpu_temp))
        actual_cpu_temp = 0
        with open(request['command'][1], 'r') as cpu_temp_file:
            actual_cpu_temp = {request['key']:cpu_temp_file.read()}
        self.assertEqual(cpu_temp, actual_cpu_temp)

    def testResolveCommand_typeRead(self):
        request = {
            'key': 'meminfo',
            'type': 'read',
            'command': ['/proc/meminfo']
        }
        meminfo = self.hm.resolve_request(request)
        actual_meminfo = {}
        with open(request['command'][0], 'r') as memfile:
            actual_meminfo = {'{}_0'.format(request['key']): memfile.read()}
        self.assertEqual(meminfo, actual_meminfo)

    def testResolveCommand_typeShellPIPE(self):
        request = {
            'key': 'mem_available',
            'type': 'shell',
            'command': [
                'cat',
                '/proc/meminfo',
                '|',
                'grep',
                'MemAvailable',
                '|',
                "awk '{print $2}'"
            ]
        }
        memavailable = self.hm.resolve_request(request)
        print('\nmemavai : ' + str(memavailable) )
        actual_memavailable = None
        with open(request['command'][1], 'r') as memfile:
            actual_memeavailable = [line for line in memfile.read().split('\n') if 'MemAvailable:' in line.split(' ')][0].split(' ')[3]
        print( '-----------' + str(actual_memavailable) )
        self.assertEqual(True, False)

        
if __name__ == '__main__':
    unittest.main()
