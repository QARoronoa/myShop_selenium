import time

import allure

from PagesObjects.HomePage import HomePage
from PagesObjects.LoginPage import LoginPage


def test_mot_de_passe_oublie(setup, mail_pwd_oublie):
    login_page = LoginPage(setup)
    home_page = HomePage(setup)


    with allure.step('cliquer sur signIn'):
        home_page.cliquer_sur_signin()

    with allure.step('cliquer sur forgot pwd'):
        login_page.cliquer_sur_forgot_password()

    with allure.step('saisir une adresse mail et cliquer sur retrieve pwd'):
        login_page.saisir_un_mail_mpd_oublie_valide()
        login_page.cliquer_sur_le_bouton_retrieve_pwd()

    with allure.step("Message confirmant l’envoi d’un email de réinitialisation"):
        login_page.verifier_que_le_mail_de_reinitialisation_est_envoye()




