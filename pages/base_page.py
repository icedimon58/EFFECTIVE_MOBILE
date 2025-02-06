import os
import time

from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import WAIT_TIME

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_dfs(self,locator):
        self.driver.execute_script("arguments[0].click();", locator)

    def _scroll_to_element(self, locator):
        element = self._find_element_on_page(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def _find_element_on_page(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)


    def _click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def _find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def _wait_visability_of_element_loading(self, locator):
        WebDriverWait(self.driver, WAIT_TIME).until(EC.visibility_of_element_located(locator))


    def _wait_text_on_element_change(self, locator, text):
        WebDriverWait(self.driver, WAIT_TIME).until(EC.text_to_be_present_in_element(locator, text))

    def _get_page_url(self):
        return self.driver.current_url

    def _get_text_from_element(self, locator):
        # self._wait_visability_of_element_loading(locator)
        return self.driver.find_element(*locator).text


    # def _set_text_to_element(self, locator, text):
    #     self.driver.find_element(*locator).send_keys(text)
    #
    # def _switch_window(self):
    #     self.driver.switch_to.window(self.driver.window_handles[-1])
