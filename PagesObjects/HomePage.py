from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PagesObjects.BasePage import BasePage

class HomePage(BasePage):


    #locators
    women_categorie = (By.XPATH, "//a[@title='Women']")
    t_shirt_sous_categorie = (By.LINK_TEXT, "T-shirts")
    logo_myShop = (By.CSS_SELECTOR, '.logo')
    bouton_signin = (By.LINK_TEXT, 'Sign in')
    barre_de_recherche = (By.ID, "search_query_top")
    bouton_rechercher = (By.NAME, "submit_search")



    def __init__(self, driver):
        super().__init__(driver)

    #methodes
    def survoler_la_categorie_women(self):
        self.survoler_un_element(self.women_categorie)

    def cliquer_sur_une_sous_categorie_tshirt(self):
        self.cliquer_sur_un_element(self.t_shirt_sous_categorie)

    def cliquer_sur_le_logo(self):
        self.cliquer_sur_un_element(self.logo_myShop)

    def cliquer_sur_signin(self):
        self.cliquer_sur_un_element(self.bouton_signin)

    def saisir_un_article_dans_la_barre_de_recherche(self, item):
        self.saisir_du_texte_dans_un_champ(self.barre_de_recherche, item)

    def cliquer_sur_le_bouton_rechercher(self):
        self.cliquer_sur_un_element(self.bouton_rechercher)

    def cliquer_sur_categorie_women(self):
        self.cliquer_sur_un_element(self.women_categorie)

    def survoler_une_categorie(self, lien_cate):
        categorie = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, lien_cate)))
        action = ActionChains(self.driver)
        action.move_to_element(categorie).perform()

    def selectionner_une_sous_cate_dresses(self, sous_cate_dresses):
        sous_categorie = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, sous_cate_dresses)))
        sous_categorie.click()

