from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import WAIT_TIME


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def _modify_locator(self, locator, num):
        xpath, locator_1 = locator
        locator_1 = locator_1.format(num)
        return xpath, locator_1

    def _wait_visability_of_element_loading(self, locator):
        WebDriverWait(self.driver, WAIT_TIME).until(expected_conditions.visibility_of_element_located(locator))

    def _get_page_url(self):
        return self.driver.current_url

    def _get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text
