from selenium.webdriver.common.by import By

from PagesObjects.BasePage import BasePage

class SearchPage(BasePage):

    #locators
    resultat_recherche = (By.CSS_SELECTOR, ".lighter")

    #methodes
    def __init__(self, driver):
        super().__init__(driver)

    def verifier_resultat_de_la_recherche(self):
        item_rechercher = self.capturer_text_element(self.resultat_recherche)
        assert "DRESS", f"item attendu DRESS, item obtenu {item_rechercher}" in item_rechercher
