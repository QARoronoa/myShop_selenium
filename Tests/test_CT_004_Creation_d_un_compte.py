import time

import allure

from PagesObjects.HomePage import HomePage
from PagesObjects.LoginPage import LoginPage
from PagesObjects.MyAccountPage import MyAccountPage


def test_creation_dun_compte(setup, mail_create_account, creation_compte_formulaire):
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    myAccount_page = MyAccountPage(setup)

    with allure.step('cliquer_sur_sign'):
        home_page.cliquer_sur_signin()

    with allure.step('Saisir un email valide dans Create an account et valider'):
        login_page.saisir_une_adresse_mail_create_account(**mail_create_account)
        login_page.cliquer_sur_create_account()

    with allure.step('Remplir tous les champs obligatoires du formulaire et soumettre'):
        login_page.remplir_formulaire_personnel_information(**creation_compte_formulaire)

    with allure.step('Compte créé, redirection My account, nom utilisateur affiché'):
        myAccount_page.verifier_titre_page('My account - My Shop')
        myAccount_page.verifier_la_presnce_message_compte_cree()
        myAccount_page.verifier_que_le_user_est_connecte()



