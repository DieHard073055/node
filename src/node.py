""" this module is responsible for handling the following
        registers the node on the server.
        parses config from the server
        loads device drivers
        handles commands from the server
        reports node health metrics to the server
"""
from utils import config_manager
from comms.mqtt.simple_mqtt_client import SimpleMqttClient
import importlib
import time

UPDATE_INTERVAL=1

mqttc = None
def initialize_driver(driver_data):
    try:
        module = importlib.import_module(driver_data['module'])
        driver = getattr(module, driver_data['name'])
        return driver(driver_data['params'])
    except ModuleNotFoundError as e:
        # Todo: log the exception
        return None


def main():
    # check if device has been registered
    # check if config file is present
    # load device drivers specified in the config file
    # setup handling of commands from the server

    # collect and publish metadata
    # collect and publish health metrics
    # collect and publish metrics from device drivers

    import ipdb; ipdb.set_trace()
    cm = config_manager.ConfigManager()
    config = cm.load_config()
    mqttc = SimpleMqttClient(
        config['device_endpoint'],
        host=config['comms']['params']['host'],
        port=config['comms']['params']['port']
    )
    mqttc.setup()

    drivers = []

    for driver in config['drivers']:
        drivers.append(initialize_driver(driver))

    for driver in drivers:
        driver.setup()

    while True:
        values = []
        try:
            for driver in drivers:
                driver.loop()
                values += driver.get_values()

        except KeyboardInterrupt as ki:
            return True
        except Exception as e:
            print(e)
            return False

        values = list(filter(None.__ne__, values))

        # publish values via mqtt
        print(values)
        time.sleep(UPDATE_INTERVAL)

if __name__ == '__main__':
    main()
