import os
import json

class BasicConfigKeyProvider(object):
    def get(self,key):
        raise NotImplementedError("Not implemented yet")

class ConfigFromEnvVariablesProvider(BasicConfigKeyProvider):
    def get(self,key):
        return os.environ.get(key)

class ConfigFromJsonProvider(BasicConfigKeyProvider):
    def __init__(self, config_path):
        self.config_data = ConfigFromJsonProvider._config_read(config_path)
    
    @staticmethod
    def _config_read(config_path):
        json_config_file = open(config_path)
        result = json.load(json_config_file)
        json_config_file.close()
        return result

    def get(self,key):
        return self.config_data.get(key)

class PriorityProvider(BasicConfigKeyProvider):
    def __init__(self, providers=None):
        self.providers = providers

    def get(self,key):
        for provider in self.providers:
            result = provider.get(key)
            if result is not None:
                return result
        return None
