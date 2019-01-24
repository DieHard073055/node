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
        value = { key : process.communicate()[0] }
        return value
