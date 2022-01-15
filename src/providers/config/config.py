from providers.config.base_config import BaseConfig
import os
from providers.config.config_provider import (
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
        self._register("EMAIL")
        self._register("PASSWORD")
        self._register("DEFAULT_TOKEN_EXPIRE")

CONFIG = Config()