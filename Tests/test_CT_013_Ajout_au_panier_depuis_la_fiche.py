import time
import allure
from PagesObjects.HomePage import HomePage
from PagesObjects.CategoriePage import CategoriePage
from PagesObjects.Article_Page import ArticlePage
from PagesObjects.BestSellerPage import BestSellerPage

def test_ajout_au_panier_depuis_fiche_fram(setup):
    home_page = HomePage(setup)
    best_sellers_page = BestSellerPage(setup)
    categorie_page = CategoriePage(setup)
    article_page = ArticlePage(setup)


    with allure.step("Cliquer sur Best Seller"):
        home_page.cliquer_sur_best_sellers()

    with allure.step("selectionner un article"):
        best_sellers_page.cliquer_sur_quick_view("Printed Chiffon Dress")

    with allure.step("modifier taille article"):
        article_page.accerder_au_frame()
        article_page.selectionner_une_taille()

    with allure.step("ajouter l article"):
        article_page.attendre_le_bouton_add_to_cart()
        article_page.quitter_frame()
        article_page.verifier_que_larticle_est_ajoute()
