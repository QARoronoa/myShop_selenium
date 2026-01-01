import allure
import locator
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self, driver):
      self.driver = driver

    @allure.step('Le titre de la page est {titreAttendu}')
    def verifier_titre_page(self, titreAttendu):
        titre = self.driver.title
        assert titre == titreAttendu, f"titre attendu {titreAttendu}, obtenu {titre} "

    @allure.step('Le texte {text} est saisie dans le champ')
    def saisir_du_texte_dans_un_champ(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
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

    def dropdown(self, locator, value):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))







        Select(element).select_by_value(str(value))

    def element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False


