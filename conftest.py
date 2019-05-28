from selenium import webdriver
import time

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeDriverManager
import pytest
from Utils import utils
import unittest


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')

@pytest.fixture()
def setup(request):
    browser = request.config.getoption('--browser')
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())

    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    elif browser.lower() == 'ie':
        driver = webdriver.Ie(IEDriverManager().install())


    elif browser.lower() == 'edge':
        driver = webdriver.Edge(EdgeDriverManager().install())


    request.cls.driver = driver
    driver.implicitly_wait(15)
    driver.maximize_window()
    driver.get(utils.url)


    yield
    driver.close()
    driver.quit()

