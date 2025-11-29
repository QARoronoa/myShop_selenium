import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from Data.LoginData import LoginData
@pytest.fixture(scope='function')
def setup():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.get('http://www.automationpractice.pl/index.php')
    driver.implicitly_wait(5)

    yield driver
    driver.quit()


@pytest.fixture
def mail_create_account():
    return LoginData.email_creation_compte()

@pytest.fixture
def creation_compte_formulaire():
    return LoginData.formulaire_create_account()

@pytest.fixture
def mail_pwd_oublie():
    return LoginData.saisir_email_mdp_oublie()