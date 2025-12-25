from selenium.webdriver.common.by import By

from PagesObjects.BasePage import BasePage

class CartPage(BasePage):

    #locators
    champ_quantite = (By.CSS_SELECTOR, ".cart_quantity_input")

    #methodes
    def __init__(self, driver):
        super().__init__(driver)

    def modifier_la_quantite(self):
        self.saisir_du_texte_dans_un_champ(self.champ_quantite, 10)