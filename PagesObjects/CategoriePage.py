from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PagesObjects.BasePage import BasePage

class CategoriePage(BasePage):

    #locators
    champ_tri = (By.ID, "selectProductSort")
    prix_articles = (By.CSS_SELECTOR, "#price")
    bouton_vue_liste = (By.CSS_SELECTOR, ".icon-th-list")

    def __init__(self, driver):
        super().__init__(driver)


    #methodes
    def effectuer_un_tri(self):
        prix = Select(self.driver.find_element(By.CSS_SELECTOR,"#selectProductSort" ))
        prix.select_by_value("price:asc")

    def basculer_en_vu_liste(self):
        self.cliquer_sur_un_element(self.bouton_vue_liste)
