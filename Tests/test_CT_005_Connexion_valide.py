import allure
from PagesObjects.HomePage import HomePage
from PagesObjects.LoginPage import LoginPage
from PagesObjects.MyAccountPage import MyAccountPage


def test_connexion_valide(setup):
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    myAccount_page = MyAccountPage(setup)

    with allure.step('cliquer_sur_sign'):
        home_page.cliquer_sur_signin()

    with allure.step('Saisir email + mot de passe valides.'):
        login_page.se_connecter()

    with allure.step('Résultat attendu : Connexion réussie, vue My account.'):
        myAccount_page.verifier_titre_myAccountPage()
        myAccount_page.verifier_que_le_user_est_connecte()
