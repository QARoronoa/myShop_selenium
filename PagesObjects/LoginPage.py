from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random

from PagesObjects.BasePage import BasePage


class LoginPage(BasePage):
    # locators
    champ_email_creation = (By.ID, "email_create")
    bouton_create_account = By.ID, "SubmitCreate"
    champ_gender = By.ID, "id_gender1"
    champ_firstName = By.ID, "customer_firstname"
    champ_lastName = By.ID, "customer_lastname"
    champ_pwd = By.ID, "passwd"
    champ_daysBirth = (By.ID, "days")
    champ_montBirth = (By.CSS_SELECTOR, "#months")
    champ_yearBirth = (By.ID, "years")
    bouton_register = (By.ID, "submitAccount")
    champ_email_connexion = (By.ID, 'email')
    champ_password = (By.ID, "passwd")
    bouton_sign_in = By.ID, "SubmitLogin"
    alert_connexion_failed = (By.CSS_SELECTOR, "div[class='alert alert-danger'] p")
    forgot_pwd_link = (By.LINK_TEXT, "Forgot your password?")
    champ_email_pwd_oublie = (By.ID, "email")
    bouton_retrieve_pwd = (By.XPATH, "(//button[@type='submit'])[2]")
    alert_message_mail_pwd_reboot = (By.CSS_SELECTOR, ".alert")

    # methodes
    def __init__(self, driver):
        super().__init__(driver)

    def saisir_une_adresse_mail_create_account(self, emailCreation):
        self.saisir_du_texte_dans_un_champ(self.champ_email_creation, emailCreation)

    def cliquer_sur_create_account(self):
        self.cliquer_sur_un_element(self.bouton_create_account)

    def remplir_formulaire_personnel_information(self, firstName, lastName, pwd, day, month, year):
        self.cliquer_sur_un_element(self.champ_gender)
        self.saisir_du_texte_dans_un_champ(self.champ_firstName, firstName)
        self.saisir_du_texte_dans_un_champ(self.champ_lastName, lastName)
        self.saisir_du_texte_dans_un_champ(self.champ_pwd, pwd)
        # days
        self.dropdown(self.champ_daysBirth, day)
        # month
        self.dropdown(self.champ_montBirth, month)
        # year
        self.dropdown(self.champ_yearBirth, year)
        #soumettre
        self.cliquer_sur_un_element(self.bouton_register)

    def se_connecter_valide(self):
        email = 'tbriand@example.org'
        mdp = '0TifRQdm@0'
        self.saisir_du_texte_dans_un_champ(self.champ_email_connexion, email)
        self.saisir_du_texte_dans_un_champ(self.champ_pwd, mdp)
        self.cliquer_sur_un_element(self.bouton_sign_in)

    def se_connecter_invalide(self):
        email = 'tbriand@esxample.org'
        mdp = '0TifssRQdm@0'
        self.saisir_du_texte_dans_un_champ(self.champ_email_connexion, email)
        self.saisir_du_texte_dans_un_champ(self.champ_pwd, mdp)
        self.cliquer_sur_un_element(self.bouton_sign_in)

    def visualiser_message_connexion_failed(self):
        message = self.capturer_text_element(self.alert_connexion_failed)
        assert message == "There is 1 error"

    def cliquer_sur_forgot_password(self):
        self.cliquer_sur_un_element(self.forgot_pwd_link)

    def saisir_un_mail_mpd_oublie_valide(self):
        email = "tbriand@example.org"
        self.saisir_du_texte_dans_un_champ(self.champ_email_pwd_oublie, email)

    def cliquer_sur_le_bouton_retrieve_pwd(self):
        self.cliquer_sur_un_element(self.bouton_retrieve_pwd)

    def verifier_que_le_mail_de_reinitialisation_est_envoye(self):
        message = self.capturer_text_element(self.alert_message_mail_pwd_reboot)
        assert message == "A confirmation email has been sent to your address: tbriand@example.org"
