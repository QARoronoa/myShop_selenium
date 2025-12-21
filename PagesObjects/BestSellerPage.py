from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PagesObjects.BasePage import BasePage
class BestSellerPage(BasePage):

    #locator
    block_article = (By.CSS_SELECTOR, ".product-container")
    bouton_quick_view = (By.CSS_SELECTOR, ".quick-view")
    nom_article = (By.CSS_SELECTOR, ".product-name")

    #methodes
    def __init__(self, driver):
        super().__init__(driver)

    def cliquer_sur_quick_view(self, product_name):
        link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,f"//a[@class='product-name' and normalize-space()='{product_name}']")))
        container = link.find_element(By.XPATH, "./ancestor::li[contains(@class,'ajax_block_product')]")

        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", container)
        ActionChains(self.driver).move_to_element(container).perform()

        quick_view = container.find_element(By.CSS_SELECTOR, "a.quick-view")
        quick_view.click()

