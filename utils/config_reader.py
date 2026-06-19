import os
import yaml
from typing import Any


class ConfigReader:
    def __init__(self, config_path: str = "config/config.yaml"):
        self.config_path = config_path
        self.config = self._load_config()
        self.environment = os.getenv("TEST_ENV", "dev")

    def _load_config(self) -> dict[str, Any]:
        with open(self.config_path, "r", encoding="utf-8") as config_file:
            return yaml.safe_load(config_file)

    def get(self, key: str, default: Any = None) -> Any:
        return self.config.get(key, default)

    def env(self) -> dict[str, Any]:
        return self.config["environments"].get(self.environment, {})

    def get_env(self, key: str, default: Any = None) -> Any:
        return self.env().get(key, default)
