import allure
from PagesObjects.HomePage import HomePage
from PagesObjects.LoginPage import LoginPage
from PagesObjects.MyAccountPage import MyAccountPage


def test_visualiser_page_commande(setup):
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    myAccount_page = MyAccountPage(setup)


    with allure.step('se connecter'):
        home_page.cliquer_sur_signin()
        login_page.se_connecter_valide()
        myAccount_page.verifier_titre_myAccountPage()
        myAccount_page.verifier_que_le_user_est_connecte()

    with allure.step("clique sur mon compte"):
        home_page.cliquer_sur_mon_compte()

    with allure.step("page historique commande"):
        myAccount_page.cliquer_sur_historique_commande()
        myAccount_page.verifier_titre_page("Order history - My Shop")

