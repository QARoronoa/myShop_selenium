import time

import allure

from PagesObjects.HomePage import HomePage
from PagesObjects.SearchPage import SearchPage

def test_recherche_article_par_mot_cle(setup):
    home_page = HomePage(setup)
    search_page = SearchPage(setup)


    with allure.step("Saisir un item dans la recherche"):
        home_page.saisir_un_article_dans_la_barre_de_recherche("dress")

    with allure.step("valider la recherche"):
        home_page.cliquer_sur_le_bouton_rechercher()

    with allure.step("redirection vers la page search"):
        search_page.verifier_titre_page("Search - My Shop")

    with allure.step("Verifier le resultat de la recherhche"):
        search_page.verifier_resultat_de_la_recherche()
