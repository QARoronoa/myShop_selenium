from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PagesObjects.BasePage import BasePage


class ArticlePage(BasePage):

    #locators
    bouton_view_large = (By.CSS_SELECTOR, ".span_link")
    couleur_orange = (By.ID, "color_13")
    champ_quantite = (By.ID, "quantity_wanted")

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

    def modifier_la_quantite(self, qauntite):
        self.saisir_du_texte_dans_un_champ(self.champ_quantite, qauntite)

    def accerder_au_frame(self):
        wait = WebDriverWait(self.driver, 20)
        frame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".fancybox-iframe")))
        self.driver.switch_to.frame(frame)
        wait.until(EC.presence_of_element_located((By.ID, "product")))

    def quitter_frame(self):
        self.driver.switch_to.default_content()

    def attendre_le_bouton_add_to_cart(self):
        wait = WebDriverWait(self.driver, 20)
        btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Add to cart']")))
        btn.click()

    def verifier_que_larticle_est_ajoute(self):
        wait = WebDriverWait(self.driver, 20)
        el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2")))








