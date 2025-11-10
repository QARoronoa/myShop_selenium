import time

import allure

from PagesObjects.CategoriePage import CategoriePage
from PagesObjects.HomePage import HomePage


def test_naviguer_vers_categories(setup):
    home_page = HomePage(setup)
    categorie_page = CategoriePage(setup)

    with allure.step('survoler la catégorie Women'):
        home_page.survoler_la_categorie_women()

    with allure.step('clique sur la catégorie tshirt'):
        home_page.cliquer_sur_une_sous_categorie_tshirt()

    with allure.step('Redirection vers la categorie Tshirt'):
        categorie_page.verifier_titre_page("T-shirts - My Shop")
