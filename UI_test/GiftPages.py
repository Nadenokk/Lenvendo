
from BaseApp import BasePage
from selenium.webdriver.common.by import By

class2 = "par-options__button par-options__button--active"

class GiftSearchLocators:

    LOCATOR_GIFT_SEARCH_NOMINAL_CARD = (By.CLASS_NAME, "par")
    LOCATOR_GIFT_SEARCH_NOMINAL500_CARD = (By.XPATH,
            "//li[@class='js-par-option par-options__item' and @data-value='500']/button")
    LOCATOR_GIFT_SEARCH_NOMINAL1000_CARD = (By.XPATH,
                                           "//li[@class='js-par-option par-options__item' and @data-value='1000']/button")
    LOCATOR_GIFT_SEARCH_NOMINAL2000_CARD = (By.XPATH,
                                            "//li[@class='js-par-option par-options__item' and @data-value='2000']/button")
    LOCATOR_GIFT_SEARCH_NOMINAL3000_CARD = (By.XPATH,
                                            "//li[@class='js-par-option par-options__item' and @data-value='3000']/button")
    LOCATOR_GIFT_SEARCH_NOMINAL5000_CARD = (By.XPATH,
                                            "//li[@class='js-par-option par-options__item' and @data-value='5000']/button")
    LOCATOR_GIFT_SEARCH_NOMINAL10000_CARD = (By.XPATH,
                                            "//li[@class='js-par-option par-options__item' and @data-value='10000']/button")
    LOCATOR_GIFT_SEARCH_NOMINAL=(By.CSS_SELECTOR, "div.page-content.container > form > input[type=hidden]:nth-child(2)")


class SearchHelper(BasePage):
    def click_on_the_500(self):
        return self.find_element(GiftSearchLocators.LOCATOR_GIFT_SEARCH_NOMINAL500_CARD,time=2).click()

    def check_name_class500(self):
        class1=self.find_element(GiftSearchLocators.LOCATOR_GIFT_SEARCH_NOMINAL500_CARD).get_attribute("class")
        assert class1 == class2

    def click_on_the_1000(self):
        return self.find_element(GiftSearchLocators.LOCATOR_GIFT_SEARCH_NOMINAL1000_CARD,time=2).click()

    def check_name_class1000(self):
        class1=self.find_element(GiftSearchLocators.LOCATOR_GIFT_SEARCH_NOMINAL1000_CARD).get_attribute("class")
        assert class1 == class2

    def click_on_the_2000(self):
        return self.find_element(GiftSearchLocators.LOCATOR_GIFT_SEARCH_NOMINAL2000_CARD,time=2).click()

    def check_name_class2000(self):
        class1=self.find_element(GiftSearchLocators.LOCATOR_GIFT_SEARCH_NOMINAL2000_CARD).get_attribute("class")
        assert class1 == class2

    def click_on_the_3000(self):
        return self.find_element(GiftSearchLocators.LOCATOR_GIFT_SEARCH_NOMINAL3000_CARD, time=2).click()

    def check_name_class3000(self):
        class1 = self.find_element(GiftSearchLocators.LOCATOR_GIFT_SEARCH_NOMINAL3000_CARD).get_attribute("class")
        assert class1 == class2

    def click_on_the_5000(self):
        return self.find_element(GiftSearchLocators.LOCATOR_GIFT_SEARCH_NOMINAL5000_CARD, time=2).click()

    def check_name_class5000(self):
        class1 = self.find_element(GiftSearchLocators.LOCATOR_GIFT_SEARCH_NOMINAL5000_CARD).get_attribute("class")
        assert class1 == class2

    def click_on_the_10000(self):
        return self.find_element(GiftSearchLocators.LOCATOR_GIFT_SEARCH_NOMINAL10000_CARD, time=2).click()

    def check_name_class10000(self):
        class1 = self.find_element(GiftSearchLocators.LOCATOR_GIFT_SEARCH_NOMINAL10000_CARD).get_attribute("class")
        assert class1 == class2

    def check_nominal(self, number):
        vvedite = self.find_element(GiftSearchLocators.LOCATOR_GIFT_SEARCH_NOMINAL).get_attribute("value")
        assert vvedite==number
