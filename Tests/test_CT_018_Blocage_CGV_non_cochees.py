import allure
from PagesObjects.HomePage import HomePage
from PagesObjects.LoginPage import LoginPage
from PagesObjects.MyAccountPage import MyAccountPage
from PagesObjects.SearchPage import SearchPage
from PagesObjects.Article_Page import ArticlePage
from PagesObjects.CartPage import CartPage
from PagesObjects.AddressPage import AdressPage
from PagesObjects.ShippingPage import ShippingPage


def test_blocage_CSV_non_cochees(setup, formulaire_adresse):
    home_page = HomePage(setup)
    login_page = LoginPage(setup)
    myAccount_page = MyAccountPage(setup)
    search_page = SearchPage(setup)
    article_page = ArticlePage(setup)
    cart_page = CartPage(setup)
    address_page = AdressPage(setup)
    shipping_page = ShippingPage(setup)



    with allure.step('se connecter'):
        home_page.cliquer_sur_signin()
        login_page.se_connecter_valide()
        myAccount_page.verifier_titre_myAccountPage()
        myAccount_page.verifier_que_le_user_est_connecte()

    with allure.step('Ajouter un article au panier'):
        home_page.saisir_un_article_dans_la_barre_de_recherche("Printed Chiffon Dress")
        home_page.cliquer_sur_le_bouton_rechercher()
        search_page.cliquer_sur_le_nom_article("Printed Chiffon Dress")
        article_page.selectionner_une_taille()
        article_page.attendre_le_bouton_add_to_cart()
        article_page.cliquer_sur_proceed_to_checkout()
        cart_page.cliquer_sur_procced_to_checkout()

    with allure.step('Cliquer sur proceed to checkout (adresse)'):
        address_page.cliquer_sur_proceed_to_checkout()

    with allure.step('Cliquer sur proceed to checkout (shipping)'):
        shipping_page.cliquer_sur_proceed_to_checkout()

    with allure.step('Verifier la presence du message d\'alerte'):
        shipping_page.verifier_la_presence_du_message_derreur_terms_non_coche()

