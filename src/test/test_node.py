""" tests which dictate the specs for the module node """
import sys
sys.path.pop(0) # remove the path for the test directory

import json
import unittest
import unittest.mock
import node
from drivers.sensors import sensor_base

'''
 mock for the config manager class
'''
exec_methods = []   # keep track of the methods thats being called.
class MockConfigManager(object):
    def __init__(self):
        global exec_methods
        exec_methods.append('__init__')
    def validate_config(self):
        global exec_methods
        exec_methods.append('validate_config')
    def save_config(self):
        global exec_methods
        exec_methods.append('save_config')
    def load_config(self):
        global exec_methods
        exec_methods.append('load_config')
        config = None
        with open('sample_config.json') as config_file:
            config = json.loads(config_file.read())
        return config

def mocked_import_module(driver_data):
    global exec_methods
    exec_methods.append('mocked_import_module')

def mocked_getattr(module_name, class_name):
    class MockedSensorClass(sensor_base.SensorBase):
        def __init__(self, params):
            exec_methods.append('mocked_driver_initiated')

        def setup(self):
            exec_methods.append('mocked_driver_setup')

        def loop(self):
            exec_methods.append('mocked_driver_loop')

        def get_values(self):
            exec_methods.append('mocked_driver_get_values')
            raise KeyboardInterrupt('end_driver_test')

    return MockedSensorClass

'''
class TestNodeStartBehaviour(unittest.TestCase):
    @unittest.mock.patch('node.getattr')
    @unittest.mock.patch('node.config_manager.ConfigManager', autospec = True)
    @unittest.mock.patch('importlib.import_module', autospec = True)
    def testMain_normalOperationConfig(self, import_module, config_manager, get_attr):
        global exec_methods
        expected_exec_methods = [
            '__init__',
            'load_config',
            'mocked_import_module',
            'mocked_driver_initiated',
            'mocked_driver_setup',
            'mocked_driver_loop',
            'mocked_driver_get_values'
        ]
        import_module.side_effect = mocked_import_module
        config_manager.side_effect = MockConfigManager
        get_attr.side_effect = mocked_getattr
        node.main()
        self.assertListEqual(exec_methods, expected_exec_methods)
'''
class TestNodeModuleImporter(unittest.TestCase):
    def setUp(self):
        health_monitor = 'drivers.sensors.health_monitor'
        config_params = []
        self.config = {
            "drivers":[
                {
                    "name":"HealthMonitor",
                    "module":health_monitor,
                    "params":config_params
                }
            ],

        }
        self.non_existent_config = {
            "drivers":[
                {
                    "name":"nonExistent",
                    "module":"non_existent.non_existent",
                    "params":config_params
                }
            ],

        }

    def testImportDriver_HealthMonitor(self):
        drivers = []
        for driver in self.config['drivers']:
            drivers.append(node.initialize_driver(driver))
        self.assertEqual(type(drivers[0]).__name__, self.config['drivers'][0]['name'])


    def testImportDriver_NonExistantModule(self):
        drivers = []
        for driver in self.non_existent_config['drivers']:
            drivers.append(node.initialize_driver(driver))
        self.assertIsNone(drivers[0])


if  __name__ == '__main__':
    unittest.main()

