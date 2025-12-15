from selenium.webdriver.common.by import By

from PagesObjects.BasePage import BasePage


class ArticlePage(BasePage):

    #locators
    bouton_view_large = (By.CSS_SELECTOR, ".span_link")

    #methodes
    def __init__(self, driver):
        super().__init__(driver)

    def cliquer_sur_le_bouton_view_larger(self):
        self.cliquer_sur_un_element(self.bouton_view_large)
