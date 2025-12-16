import time

import allure
from PagesObjects.HomePage import HomePage
from PagesObjects.CategoriePage import CategoriePage
from PagesObjects.Article_Page import ArticlePage

def test_selection_varation_quantite(setup):
    home_page = HomePage(setup)
    categorie_page = CategoriePage(setup)
    article_page = ArticlePage(setup)

    with allure.step("Survoler une categorie"):
        home_page.survoler_une_categorie("DRESSES")

    with allure.step("Selection sous categorie dresses"):
        home_page.selectionner_une_sous_cate_dresses("SUMMER DRESSES")

    with allure.step("Ouvrir la fiche produit printed summer dress"):
        categorie_page.ouvrir_la_fiche_dune_dress("Printed Summer Dress")

    with allure.step("selectionner une taille"):
        article_page.selectionner_une_taille()
        time.sleep(1)
        article_page.selectionner_la_couleur_orange()
