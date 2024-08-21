import os

import pytest
import dotenv
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def load_env():
    dotenv.load_dotenv()


@pytest.fixture
def login():
    return os.getenv("LOGIN")


@pytest.fixture
def token():
    return os.getenv("TOKEN")


@pytest.fixture
def domain():
    return "en.wikipedia.org"


@pytest.fixture
def driver():
    """
    The fixture that our tests call to get access to a driver.
    """

    driver = webdriver.Firefox()

    yield driver

    driver.quit()
