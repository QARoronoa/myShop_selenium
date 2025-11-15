from selenium.webdriver.common.by import By

from PagesObjects.BasePage import BasePage


class MyAccountPage(BasePage):

    #locators
    success_message_compte_created = (By.CSS_SELECTOR, ".alert-success")
    nom_utilisateur = (By.CSS_SELECTOR, '.account')


    def __init__(self, driver):
        super().__init__(driver)

    #Methodes

    def verifier_titre_myAccountPage(self):
        self.verifier_titre_page('My account - My Shop')

    def verifier_la_presnce_message_compte_cree(self):
        texte = self.capturer_text_element(self.success_message_compte_created)
        assert texte == "Your account has been created."

    def verifier_que_le_user_est_connecte(self):
        self.element_visible(self.nom_utilisateur)
