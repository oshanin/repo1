from base_config import BaseConfig
import os
from providers.data.config_provider import (
    ConfigFromJsonProvider,
    ConfigFromEnvVariablesProvider,
    PriorityProvider,
)

class Config(BaseConfig):
    DEFAULT_ENV = "prod"

    def __init__(self):
        self.config_dict = {}
    
        json_config_path = F"src/target_configs/{os.environ.get('TARGET', self.DEFAULT_ENV)}.json"

        app_env_var = ConfigFromEnvVariablesProvider()
        app_json_config = ConfigFromJsonProvider(json_config_path)

        self.config_provider = PriorityProvider([app_env_var,app_json_config])

        super(Config, self).__init__()

        self._register("BASE_URL")

CONFIG = Config()