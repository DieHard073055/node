""" this module is responsible for handling the following
        registers the node on the server.
        parses config from the server
        loads device drivers
        handles commands from the server
        reports node health metrics to the server
"""
from utils import config_manager

def main():
    # check if device has been registered
    # check if config file is present
    # load device drivers specified in the config file
    # setup handling of commands from the server

    # collect and publish metadata
    # collect and publish health metrics
    # collect and publish metrics from device drivers

    cm = config_manager.ConfigManager()
    cm.validate_config()
    cm.save_config()

if __name__ == '__main__':
    main()
