import json
class ConfigManager(object):
    def __init__(self):
        self.config_file = 'sample_config.json'
        print('initiated config manager')

    def validate_config(self):
        print('config parsed')

    def save_config(self):
        print('config file saved')

    def load_config(self):
        config = None
        with open(self.config_file) as config_file:
            config = json.loads(config_file.read())
        return config


