import allure

from PagesObjects.HomePage import HomePage
from PagesObjects.LoginPage import LoginPage

def test_connexion_invalide(setup):
    home_page = HomePage(setup)
    login_page = LoginPage(setup)

    with allure.step('cliquer sur signin'):
        home_page.cliquer_sur_signin()


    with allure.step('Saisir email/mot de passe invalides'):
        login_page.se_connecter_invalide()

    with allure.step('Message d’erreur explicite, pas de connexion'):
        login_page.visualiser_message_connexion_failed()