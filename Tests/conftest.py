import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import os
from Config.config import TestData

# pytest_addoption allows users to register a user-defined command line parameter to facilitate users to pass data to pytest
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=TestData.BROWSER)

@pytest.fixture(scope='class')
def getBrowser(request):
    # config.getoption gets parameter values (from config file or from command line arguments)
    browser = request.config.getoption("--browser")
    return browser

# 'init_driver' class scope fixture using another class scope fixture 'getBrowser'
@pytest.fixture(scope='class')
def init_driver(request, getBrowser):
    
    # TEST SETUP STEPS

    #get driver path, where browser driver needs to be installed or maintained
    # os.path.dirname(__file__) - gets current file directory path , i.e. - C:\Mk_projects\python_selenium_automation_framework\Tests\
    # os.path.join(os.path.dirname(__file__), '..', 'Drivers' - from current directory, creates relative path to Drivers folder, i.e. - C:\Mk_projects\python_selenium_automation_framework\Tests\..\Drivers 
    # os.path.realpath - generates absolute path to Drivers folder, i.e. - C:\Mk_projects\python_selenium_automation_framework\Drivers
    driver_path = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'Drivers'))
    print(driver_path)
    driver_log_path = os.path.join(driver_path, 'logs')
    print(driver_log_path)
    
    # cross browser testing support
    driver=None
    if getBrowser == "firefox":
        # using gecko driver manager to automatically download and install respective compatible gecko driver
        driver = webdriver.Firefox(service=FireFoxService(GeckoDriverManager(path=driver_path).install(), log_path=driver_log_path))
        request.cls.driver = driver
    elif getBrowser == "chrome":
        # using chrome driver manager to automatically download and install respective compatible chrome driver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(path=driver_path).install(), log_path=driver_log_path))
        request.cls.driver = driver
    elif getBrowser == 'edge':
        # using edge driver manager to automatically download and install respective compatible edge driver
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager(path=driver_path).install(), log_path=driver_log_path))
        request.cls.driver = driver
    
    yield
    # TEST TEARDOWN STEPS
    driver.close()