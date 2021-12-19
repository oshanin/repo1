class BaseConfig:
    def __init__(self) -> None:
        self.config_dict = {}

    def _register(self,key):
        self.config_dict[key] = self.config_provider.get(key)

    def __getattr__(self, item):
        if item in self.config_dict:
            return self.config_dict[item]
        raise AttributeError("Variable has to be registered prior to usage!")
