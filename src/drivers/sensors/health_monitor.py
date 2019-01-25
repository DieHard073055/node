""" Provides a generic interface to monitor various types of health merics. Can be configured via the config parameters which is passed into this module."""

__author__ = 'Eshan Shafeeq'

import subprocess

class HealthMonitor():
    '''
        this class will obtain all the health metrics
        defined in the param section of the config
        passed in
    '''

    def __init__(self, config_params):
        self.config_params = config_params

    def _exec_shell(self, key, commands):
        value = None
        process = subprocess.Popen(commands, stdout=subprocess.PIPE)
        value = { key : process.communicate()[0].decode('utf-8') }
        return value

    def _read_file(self, key, commands):
        value = None
        for command in commands:
            with open( command, 'r') as cfile:
                value = { key: cfile.read() }
        return value

    def resolve_request(self, request):
        if request['type'] == 'shell':
            return self._exec_shell(request['key'], request['command'])
        elif request['type'] == 'read':
            return self._read_file(request['key'], request['command'])
        else:
            return None
        
