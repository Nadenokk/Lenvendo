import allure

from GiftPages import SearchHelper

@allure.feature('Choice 500')
@allure.story('Выбор номинала 500')
def test_gift_500(browser):
    gift_main_page = SearchHelper(browser)
    gift_main_page.go_to_site()
    gift_main_page.scroll_to_element()
    gift_main_page.click_on_the_500()
    gift_main_page.check_name_class500()
    gift_main_page.check_nominal("500")

@allure.feature('Choice all')
@allure.story('Выбор всех номиналов')
def test_gift_all(browser):
    gift_main_page = SearchHelper(browser)
    gift_main_page.go_to_site()
    gift_main_page.scroll_to_element()
    gift_main_page.click_on_the_500()
    gift_main_page.check_name_class500()
    gift_main_page.check_nominal("500")
    gift_main_page.click_on_the_1000()
    gift_main_page.check_name_class1000()
    gift_main_page.check_nominal("1000")
    gift_main_page.click_on_the_2000()
    gift_main_page.check_name_class2000()
    gift_main_page.check_nominal("2000")
    gift_main_page.click_on_the_3000()
    gift_main_page.check_name_class3000()
    gift_main_page.check_nominal("3000")
    gift_main_page.click_on_the_5000()
    gift_main_page.check_name_class5000()
    gift_main_page.check_nominal("5000")
    gift_main_page.click_on_the_10000()
    gift_main_page.check_name_class10000()
    gift_main_page.check_nominal("10000")