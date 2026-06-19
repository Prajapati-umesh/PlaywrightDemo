import os
from pathlib import Path

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright

from utils.config_reader import ConfigReader
from utils.logger_util import create_logger


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default=os.getenv("TEST_ENV", "dev"),
        help="Environment to run tests against (dev, qa, prod)",
    )


@pytest.fixture(scope="session")
def config():
    config_reader = ConfigReader()
    return config_reader


@pytest.fixture(scope="session")
def logger(config):
    log_file = config.get("logging", {}).get("file", "artifacts/logs/framework.log")
    return create_logger("framework", log_file, config.get("logging", {}).get("level", "INFO"))


@pytest.fixture(scope="session")
def playwright_context(config):
    env = config.env()
    with sync_playwright() as playwright:
        browser = getattr(playwright, env.get("browser", "chromium")).launch(
            headless=env.get("headless", True)
        )
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


@pytest.fixture(scope="function")
def page(playwright_context: BrowserContext) -> Page:
    page = playwright_context.new_page()
    yield page
    page.close()
