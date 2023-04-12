import pytest
from selene import browser


@pytest.fixture(scope="session")
def browser_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1920
    browser.open('https://google.com')