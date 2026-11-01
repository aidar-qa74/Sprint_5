

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

@pytest.fixture(scope='function')
def driver_chrome():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 60)
    chrome_options = webdriver.ChromeOptions()
    time.sleep(5)
    yield driver
    driver.quit()