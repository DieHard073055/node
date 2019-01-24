"""Provides the common interface for all the device drivers."""

__version__ = 0.1
__author__ = 'Eshan Shafeeq'

import abc

class DriverBase():
    ''' DriverBase

        methods
        -------

        setup() : will be invoked once to initialize the driver.
        loop()  : will be invoked once for every iteration of the node main loop.
    '''
    @abc.abstractmethod
    def setup(self):
        '''Do all the initializations for the device driver here.'''

    @abc.abstractmethod
    def heartbeat_tick(self):
        '''Run the main operations for the device driver.'''
