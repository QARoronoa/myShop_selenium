from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PagesObjects.BasePage import BasePage

class ShippingPage(BasePage):

    case_terms_conditions = By.ID, "cgv"
    bouton_procced_to_checkout = (By.CSS_SELECTOR, "button[name='processCarrier']")
    message_alerte_terms_conditions = (By.CSS_SELECTOR, "p.fancybox-error")
    def __init__(self, driver):
        super().__init__(driver)

    def accepter_terms_conditions(self):
        self.cliquer_sur_un_element(self.case_terms_conditions)

    def cliquer_sur_proceed_to_checkout(self):
        self.cliquer_sur_un_element(self.bouton_procced_to_checkout)

    def verifier_la_presence_du_message_derreur_terms_non_coche(self):
        mess = self.capturer_text_element(self.message_alerte_terms_conditions)
        assert mess == "You must agree to the terms of service before continuing."