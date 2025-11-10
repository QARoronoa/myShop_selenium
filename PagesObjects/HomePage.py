from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from PagesObjects.BasePage import BasePage

class HomePage(BasePage):


    #locators
    women_categorie = (By.XPATH, "//a[@title='Women']")
    t_shirt_sous_categorie = (By.LINK_TEXT, "T-shirts")

    def __init__(self, driver):
        super().__init__(driver)

    #methodes
    def survoler_la_categorie_women(self):
        self.survoler_un_element(self.women_categorie)


    def cliquer_sur_une_sous_categorie_tshirt(self):
        self.cliquer_sur_un_element(self.t_shirt_sous_categorie)
