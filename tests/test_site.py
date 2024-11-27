import time
from pages.homepage import HomePage
from pages.productpage import ProductPage



def test_open_galaxy_s6(driver):

    homePage = HomePage(driver)
    homePage.open()
    homePage.click_galaxy_s6()
    productPage = ProductPage(driver)
    productPage.check_title_is('Samsung galaxy s6')


def test_two_monitors(driver):
    homePage = HomePage(driver)
    homePage.open()
    homePage.click_monitor()

    time.sleep(3)

    homePage.check_product_count(2)


