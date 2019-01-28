""" Tests for the health_monitor """

__author__ = 'Eshan Shafeeq'

import unittest
from drivers.sensors import health_monitor


class TestHealthMonitorResolveRequests(unittest.TestCase):
    """Unittests to evaluate the responses for the requests"""

    def setUp(self):
        self.health_monitor = health_monitor.HealthMonitor([])

    def testResolveRequest_typeShell(self):
        actual_temp_file = '/sys/class/thermal/thermal_zone0/temp'
        tmp_temp_file = './cpu_temp'
        request = {
            'key': 'cpu_temp_0',
            'type': 'shell',
            'command': ['cat', tmp_temp_file]
        }

        with open(actual_temp_file, 'r') as cpu_temp_file:
            with open(tmp_temp_file, 'w') as tmp_file:
                tmp_file.write(cpu_temp_file.read())


        actual_cpu_temp = 0
        with open(tmp_temp_file, 'r') as cpu_temp_file:
            actual_cpu_temp = {request['key']:str(cpu_temp_file.read()).rstrip()}

        cpu_temp = self.health_monitor.resolve_request(request)
        self.assertEqual(cpu_temp, actual_cpu_temp)

    def testResolveRequest_typeRead(self):
        actual_mem_file = '/proc/meminfo'
        tmp_mem_file = './memfile'
        request = {
            'key': 'meminfo',
            'type': 'read',
            'command': [tmp_mem_file]
        }
        actual_meminfo = {}
        with open(actual_mem_file, 'r') as memfile:
            with open(tmp_mem_file, 'w') as tmp_file:
                tmp_file.write(memfile.read())

        with open(tmp_mem_file, 'r') as memfile:
            actual_meminfo = {'{}_0'.format(request['key']): memfile.read().rstrip()}

        meminfo = self.health_monitor.resolve_request(request)
        self.assertEqual(meminfo, actual_meminfo)

    def testResolveRequest_typeShellPIPE(self):
        actual_mem_file = '/proc/meminfo'
        tmp_mem_file = './memfile'
        request = {
            'key': 'mem_available',
            'type': 'shell',
            'command': [
                'cat',
                tmp_mem_file,
                '|',
                'grep',
                'MemAvailable',
                '|',
                "awk '{print $2}'"
            ]
        }
        with open(actual_mem_file, 'r') as memfile:
            with open(tmp_mem_file, 'w') as tmp_file:
                tmp_file.write(memfile.read())


        memavailable = self.health_monitor.resolve_request(request)
        actual_memavailable = None
        with open(request['command'][1], 'r') as memfile:
            actual_memavailable = [
                line for line in memfile.read().split('\n')
                if 'MemAvailable:' in line.split(' ')
            ][0].split(' ')[3]
            actual_memavailable = {request['key']: actual_memavailable}
        self.assertEqual(memavailable, actual_memavailable)

class TestHealthMonitorImplementation(unittest.TestCase):
    def setUp(self):
        self.health_monitor = health_monitor.HealthMonitor([])
        self.health_monitor_cputemp = health_monitor.HealthMonitor([
            {
                'key': 'cpu_temp_0',
                'type': 'shell',
                'command': ['cat', '/sys/class/thermal/thermal_zone0/temp']
            }
        ])

    def testLoop_emptyConfigParams(self):
        self.health_monitor.loop()

    def testLoop_getCPUTempRequest(self):
        self.health_monitor_cputemp.loop()

    def testGetValues_emptyConfigParams(self):
        self.health_monitor.get_values()

    def testGetValues_getCPUTempRequest(self):
        self.health_monitor_cputemp.get_values()

if __name__ == '__main__':
    unittest.main()
