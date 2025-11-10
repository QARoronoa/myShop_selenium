import allure
import locator
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self, driver):
      self.driver = driver

    @allure.step('Le titre de la page est {titreAttendu}')
    def verifier_titre_page(self, titreAttendu):
        titre = self.driver.title
        assert titre == titreAttendu, f"titre attendu {titreAttendu}, obtenu {titre} "


    def cliquer_sur_un_element(self, locator: locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        element.click()

    def capturer_text_element(self, locator: locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        element_text = element.text
        return element_text

    def survoler_un_element(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        actions = ActionChains(self.driver).move_to_element(element).perform()
