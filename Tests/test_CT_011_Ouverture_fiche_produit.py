import allure
from PagesObjects.HomePage import HomePage
from PagesObjects.CategoriePage import CategoriePage
from PagesObjects.Article_Page import ArticlePage

def test_ouverture_fiche_produit(setup):
    home_page = HomePage(setup)
    categorie_page = CategoriePage(setup)
    article_page = ArticlePage(setup)

    with allure.step("Ouverture fiche produit"):
        home_page.survoler_la_categorie_women()
        home_page.cliquer_sur_une_sous_categorie_tshirt()
        categorie_page.ouvrir_la_fiche_produit("Faded Short")
        article_page.cliquer_sur_le_bouton_view_larger()
        article_page.verifier_titre_page("Faded Short Sleeve T-shirts - My Shop")




