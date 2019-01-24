""" tests which dictate the specs for the module node """
import unittest
from unittest import TestCase
from unittest.mock import patch
import node

'''
 mock for the config manager class
'''

exec_methods = []
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


class TestNodeStartBehaviour(TestCase):
    @patch('node.config_manager.ConfigManager', autospec = True)
    def test_node_starting(self, mcm):
        global exec_methods
        mcm.side_effect = MockConfigManager
        node.main()
        self.assertListEqual(exec_methods, ['__init__', 'validate_config', 'save_config'])

if  __name__ == '__main__':
    unittest.main()

