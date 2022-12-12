import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import os
from Config.config import TestData

@pytest.fixture(scope='class')
def init_driver(request):
    #get driver path, where gecko driver needs to be installed or maintained
    driver_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'Drivers'))
    print(driver_path)
    driver_log_path = os.path.join(driver_path, 'logs')
    print(driver_log_path)

    # using gecko driver manager to automatically download and install respective compatible gecko driver
    driver = webdriver.Firefox(service=Service(GeckoDriverManager(path=driver_path).install(), log_path=driver_log_path))
    request.cls.driver = driver
    yield
    driver.close()