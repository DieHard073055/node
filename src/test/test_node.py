""" tests which dictate the specs for the module node """
import unittest
import unittest.mock
import node
import sys

sys.path.pop(0) # remove the path for the test directory

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


class TestNodeStartBehaviour(unittest.TestCase):
    @unittest.mock.patch('node.config_manager.ConfigManager', autospec = True)
    def testMain_normalOperation(self, mcm):
        global exec_methods
        mcm.side_effect = MockConfigManager
        node.main()
        self.assertListEqual(exec_methods, ['__init__', 'validate_config', 'save_config'])

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
            driver.append(node.initialize_driver(driver))
        self.assertIsNone(driver[0])


if  __name__ == '__main__':
    unittest.main()

