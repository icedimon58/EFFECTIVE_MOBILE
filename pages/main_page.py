import allure

from locators.main_page_locators import ABOUT_US_LOCATOR,SERVISES_LOCATOR,PROJECTS_LOCATOR,REVIEWS_LOCATOR,CONTACTS_LOCATOR
from pages.base_page import BasePage


class MainPage(BasePage):
    # @allure.step("Ожидание загрузки страницы")
    # def load_page(self):
    #     return self._get_text_from_element(ABOUT_US_LOCATOR)

    @allure.step("Получение URL страницы")
    def get_url(self):
        return self._get_page_url()

    @allure.step("Клик по элементу ")
    def click_on_link(self,locator):
        self._click_on_element(locator)



    @allure.step("Слайд до элемента ")
    def wait_element_on_page(self,locator):
        self._wait_visability_of_element_loading(locator)
        # self._scroll_to_element(locator)

    @allure.step("Клик по элементу ")
    def get_element_text(self,locator):
        return self._get_text_from_element(locator)

    @allure.step("Клик по элементу ")
    def get_element_text2(self,locator):
        return self._get_text_from_element(locator)


    #
    # @allure.step("Клик по элементу 'Услуги'")
    # def click_on_service_link(self):
    #     self._click_on_element(SERVISES_LOCATOR)
    #
    # @allure.step("Клик по элементу 'Проекты'")
    # def click_on_projects_link(self):
    #     self._click_on_element(PROJECTS_LOCATOR)
    #
    # @allure.step("Клик по элементу 'Отзывы'")
    # def click_on_review_link(self):
    #     self._click_on_element(REVIEWS_LOCATOR)
    #
    # @allure.step("Клик по элементу 'Контакты'")
    # def click_on_contact_link(self):
    #     self._click_on_element(CONTACTS_LOCATOR)