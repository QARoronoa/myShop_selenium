import allure
from PagesObjects.HomePage import HomePage
from PagesObjects.CategoriePage import CategoriePage

def test_tri_et_mode_affichage(setup):
    home_page = HomePage(setup)
    categorie_page = CategoriePage(setup)


    with allure.step("cliquer sur women catégorie"):
        home_page.cliquer_sur_categorie_women()

    with allure.step("Redirection vers la page women"):
        home_page.verifier_titre_page("Women - My Shop")

    with allure.step("Faire un tri Lowest first"):
        categorie_page.effectuer_un_tri()

    with allure.step('basculer en vue liste'):
        categorie_page.basculer_en_vu_liste()




