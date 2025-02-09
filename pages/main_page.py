import allure

from data import HEADERS_LINK
from locators.main_page_locators import MENU_LOCATOR
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Получение URL страницы")
    def get_url(self):
        return self._get_page_url()

    @allure.step("Модифицируем локатор")
    def modify_locator(self, locator, num):
        return self._modify_locator(locator, HEADERS_LINK[num])

    @allure.step("Клик в верхнем меню страницы")
    def main_menu_click(self):
        self._click_on_element(MENU_LOCATOR)

    @allure.step("Клик по элементу")
    def click_on_link(self, locator):
        self._click_on_element(locator)

    @allure.step("Скролл до элемента")
    def wait_element_on_page(self, locator):
        self._wait_visability_of_element_loading(locator)

    @allure.step("Получаем текст элемента")
    def get_element_text(self, locator):
        return self._get_text_from_element(locator)
