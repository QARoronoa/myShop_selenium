from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PagesObjects.BasePage import BasePage


class ArticlePage(BasePage):

    #locators
    bouton_view_large = (By.CSS_SELECTOR, ".span_link")
    couleur_orange = (By.ID, "color_13")

    #methodes
    def __init__(self, driver):
        super().__init__(driver)

    def cliquer_sur_le_bouton_view_larger(self):
        self.cliquer_sur_un_element(self.bouton_view_large)

    def selectionner_une_taille(self):
        taille = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "select#group_1")))
        dropdown = Select(taille)
        dropdown.select_by_value("3")

    def selectionner_la_couleur_orange(self):
        self.cliquer_sur_un_element(self.couleur_orange)