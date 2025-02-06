import allure
import pytest
from data import *
from locators.main_page_locators import *
from pages.main_page import MainPage


class TestEffectiveMobilePage:

    @allure.description('Проверяем header на главной странице')
    @allure.title('Проверка главной страницы')
    @pytest.mark.parametrize('locator,expected_url,exp_locator,expected_text', [
        [ABOUT_US_LOCATOR, PAGE_URL + ABOUT_US_LINK, ABOUT_US_TEXT_LOCATOR, ABOUT_EXPECTED_TEXT],
        [SERVISES_LOCATOR, PAGE_URL + SERVISES_LINK, SERVICE_TEXT_LOCATOR, SERVICE_EXECTED_TEXT],
        [REVIEWS_LOCATOR, PAGE_URL + REVIEWS_LINK, REVIEWS_TEXT_LOCATOR, REVIEWS_EXPECTED_TEXT],
        [CONTACTS_LOCATOR, PAGE_URL + CONTACTS_LINK, CONTACTS_TEXT_LOCATOR, CONTACTS_EXPECTED_TEXT],
        [SPECIALIST_LOCATOR, PAGE_URL + SPECIALIST_LINK, SPECIALIST_TEXT_LOCATOR, SPECIALIST_EXPECTED_TEXT],
        [PROJECTS_LOCATOR, PAGE_URL + PROJECTS_LINK, PROJECTS_TEXT_LOCATOR, PROJECTS_EXPECTED_TEXT]
    ])
    def test_check_main_window(self, page_driver, locator, expected_url, exp_locator, expected_text):
        main_page = MainPage(page_driver)
        main_page.click_on_link(locator)
        main_page.wait_element_on_page(exp_locator)
        page_url = main_page.get_url()
        text_from_element = main_page.get_element_text(exp_locator)
        # print(text_from_element)
        # print(page_url)
        assert page_url == expected_url and expected_text == text_from_element
