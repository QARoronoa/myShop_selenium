import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope='function')
def setup():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.get('http://www.automationpractice.pl/index.php')
    driver.implicitly_wait(5000)

    yield driver
    driver.close()
