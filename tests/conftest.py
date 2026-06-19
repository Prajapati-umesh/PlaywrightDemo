import os
from pathlib import Path

import pytest

from utils.config_reader import ConfigReader


@pytest.fixture(scope="session")
def config():
    config_path = Path(__file__).resolve().parents[1] / "config" / "config.yaml"
    return ConfigReader(str(config_path))


def pytest_configure(config):
    reports_dir = Path("reports")
    artifacts_dir = Path("artifacts")
    reports_dir.mkdir(parents=True, exist_ok=True)
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    (artifacts_dir / "logs").mkdir(parents=True, exist_ok=True)
