"""Provides the common interface for all the sensor drivers."""

__version__ = 0.1
__author__ = 'Eshan Shafeeq'

import abc
from drivers import driver_base

class SensorBase(driver_base.DriverBase):
    ''' SensorBase

    methods
    -------

    setup()         : will be invoked to initialize the sensor driver.
    loop()          : will be invoked once to wakeup the sensor to collect measurements.
    get_values()    : will be invoked to request all the sensor measurements.

    '''
    @abc.abstractmethod
    def setup(self):
        '''initialize the sensor module here.'''

    @abc.abstractmethod
    def loop(self):
        '''collect all the sensor values here.'''

    @abc.abstractmethod
    def get_values(self):
        '''return all the collected sensor values in a tuple.'''
