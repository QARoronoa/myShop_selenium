from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PagesObjects.BasePage import BasePage

class SearchPage(BasePage):

    #locators
    resultat_recherche = (By.CSS_SELECTOR, ".lighter")
    bouton_more = (By.XPATH, "//*[text()='More']")

    #methodes
    def __init__(self, driver):
        super().__init__(driver)

    def verifier_resultat_de_la_recherche(self):
        item_rechercher = self.capturer_text_element(self.resultat_recherche)
        assert "DRESS", f"item attendu DRESS, item obtenu {item_rechercher}" in item_rechercher

    def cliquer_sur_le_nom_article(self, item):
        article = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, item)))
        article.click()

