""" Provides a generic interface to monitor various types of health merics. Can be configured via
the config parameters which is passed into this module."""

__author__ = 'Eshan Shafeeq'

import subprocess
from drivers.sensors import sensor_base

class HealthMonitor(sensor_base.SensorBase):
    '''
        this class will obtain all the health metrics
        defined in the param section of the config
        passed in
    '''

    def __init__(self, config_params):
        self.config_params = config_params

    def _exec_shell(self, key, commands):
        value = None
        process = subprocess.Popen(' '.join(commands), shell=True, stdout=subprocess.PIPE)
        value = { key : process.communicate()[0].decode('utf-8').rstrip() }
        return value

    def _read_file(self, key, commands):
        value = []
        index=0
        for command in commands:
            with open( command, 'r') as cfile:
                value = { '{}_{}'.format(key, index): cfile.read().rstrip() }
                index+=1
        return value

    def resolve_request(self, request):
        if request['type'] == 'shell':
            return self._exec_shell(request['key'], request['command'])
        elif request['type'] == 'read':
            return self._read_file(request['key'], request['command'])
        else:
            return None

    def setup(self):
        self.values = None

    def loop(self):

        for request in self.config_params:
            if not self.values:
                self.values = []
            self.values.append(self.resolve_request(request))

    def get_values(self):
        return self.values
