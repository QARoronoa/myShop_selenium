import time

import allure
from PagesObjects.Article_Page import ArticlePage
from PagesObjects.BestSellerPage import BestSellerPage
from PagesObjects.HomePage import HomePage
from PagesObjects.CartPage import CartPage

def test_suppression_article_panier(setup):
    home_page = HomePage(setup)
    best_sellers_page = BestSellerPage(setup)
    article_page = ArticlePage(setup)
    cart_page = CartPage(setup)


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
        article_page.verifier_la_presence_du_bouton_proceed_checkout()

    with allure.step("Cliquer sur proceed to checkout"):
        article_page.cliquer_sur_proceed_to_checkout()


    with allure.step("supprimer l'article"):
        cart_page.cliquer_sur_le_bouton_delete()

    with allure.step("verifier le message panier vide"):
        cart_page.verifier_la_presence_message_panier_vide()

        time.sleep(6)
