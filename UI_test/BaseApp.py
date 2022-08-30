from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://HR:test@qa.digift.ru/"

    def scroll_to_element(self, time=10):
        """ Scroll page to the element. """
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.wrapper > div.page-content.container > form > div.par")),
                                                         message=f"Can't find element by locator")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        with allure.step(f'GET request to: {self.base_url}'):
            return self.driver.get(self.base_url)
