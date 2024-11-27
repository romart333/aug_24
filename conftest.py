from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)

    yield driver
    driver.close()
