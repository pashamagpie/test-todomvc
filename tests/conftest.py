import pytest
from selene.support.shared import browser

from test_todomvc import config


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.browser_name = config.options.BROWSER_NAME
    yield
    if config.options.BROWSER_QUIT:
        browser.quit()
    else:
        browser.clear_local_storage()
