from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from PagesObjects.BasePage import BasePage

class AdressPage(BasePage):

    champ_city = (By.XPATH, "//input[@id='city']")
    champ_adr1 = (By.ID,"address1")
    champ_state = (By.XPATH,"//select[@id='id_state']")
    champ_cp = (By.XPATH,"//input[@id='postcode']")
    champ_phone = (By.XPATH,"//input[@id='phone']")
    champ_mobile = (By.XPATH,"//input[@id='phone_mobile']")
    champ_alias = (By.XPATH,"//input[@id='alias']")
    bouton_save = (By.XPATH,"//span[normalize-space()='Save']")
    bouton_procced_to_checkout = (By.CSS_SELECTOR, "button[name='processAddress']")
    def __init__(self, driver):
        super().__init__(driver)

    def remplir_le_formlaire(self, adr1, city, address_title):
        self.saisir_du_texte_dans_un_champ(self.champ_adr1, adr1)
        self.saisir_du_texte_dans_un_champ(self.champ_city, city )

        dropdown = Select(self.driver.find_element(By.ID, "id_state"))
        dropdown.select_by_value("8")

        self.saisir_du_texte_dans_un_champ(self.champ_cp, 92350)
        self.saisir_du_texte_dans_un_champ(self.champ_phone, "898989898898")
        self.saisir_du_texte_dans_un_champ(self.champ_mobile, "898989898898")
        self.saisir_du_texte_dans_un_champ(self.champ_alias, address_title)
        self.cliquer_sur_un_element(self.bouton_save)

    def cliquer_sur_proceed_to_checkout(self):
        self.cliquer_sur_un_element(self.bouton_procced_to_checkout)
