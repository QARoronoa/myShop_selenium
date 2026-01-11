from selenium.webdriver.common.by import By

from PagesObjects.BasePage import BasePage

class CartPage(BasePage):

    #locators
    champ_quantite = (By.CSS_SELECTOR, ".cart_quantity_input")
    bouton_delete = (By.CSS_SELECTOR, ".cart_quantity_delete")
    message_panier_vide = (By.CSS_SELECTOR, ".alert-warning")
    bouton_proceed_to_checout = (By.LINK_TEXT, "Proceed to checkout")

    #methodes
    def __init__(self, driver):
        super().__init__(driver)

    def modifier_la_quantite(self):
        self.saisir_du_texte_dans_un_champ(self.champ_quantite, 10)

    def cliquer_sur_le_bouton_delete(self):
        self.cliquer_sur_un_element(self.bouton_delete)

    def verifier_la_presence_message_panier_vide(self):
        message = self.capturer_text_element(self.message_panier_vide)
        assert message == "Your shopping cart is empty."

    def cliquer_sur_procced_to_checkout(self):
        self.cliquer_sur_un_element(self.bouton_proceed_to_checout)