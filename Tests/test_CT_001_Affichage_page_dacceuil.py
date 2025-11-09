import allure
from PagesObjects.HomePage import HomePage


def test_afficher_la_page_dacceuil(setup):
    home_page = HomePage(setup)

    with allure.step('verifier le titre de la page'):
        home_page.verifier_titre_page('My Shop')

