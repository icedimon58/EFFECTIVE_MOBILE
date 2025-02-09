import allure
import pytest
from data import *
from locators.main_page_locators import *
from pages.main_page import MainPage


class TestEffectiveMobilePage:

    @allure.description('Проверяем всплывающее меню на главной странице')
    @allure.title('Проверка главной страницы в разрешении 900х1080')
    @pytest.mark.parametrize('page_driver', ['900'], indirect=True)
    @pytest.mark.parametrize('locator,expected_url,exp_locator,expected_text,resolution', [
        [ABOUT_US_LOCATOR, PAGE_URL + ABOUT_US_LINK, ABOUT_US_TEXT_LOCATOR, ABOUT_EXPECTED_TEXT, 0],
        [SERVISES_LOCATOR, PAGE_URL + SERVISES_LINK, SERVICE_TEXT_LOCATOR, SERVICE_EXECTED_TEXT, 0],
        [REVIEWS_LOCATOR, PAGE_URL + REVIEWS_LINK, REVIEWS_TEXT_LOCATOR, REVIEWS_EXPECTED_TEXT, 0],
        [CONTACTS_LOCATOR, PAGE_URL + CONTACTS_LINK, CONTACTS_TEXT_LOCATOR, CONTACTS_EXPECTED_TEXT, 0],
        [PROJECTS_LOCATOR, PAGE_URL + PROJECTS_LINK, PROJECTS_TEXT_LOCATOR, PROJECTS_EXPECTED_TEXT, 0]
    ])
    def test_check_main_window_900_1080(self, page_driver, locator, expected_url, exp_locator, expected_text,
                                        resolution):
        main_page = MainPage(page_driver)
        main_page.main_menu_click()
        locator = main_page.modify_locator(locator, resolution)
        main_page.wait_element_on_page(locator)
        main_page.click_on_link(locator)
        page_url = main_page.get_url()
        main_page.wait_element_on_page(exp_locator)
        text_from_element = main_page.get_element_text(exp_locator)
        assert page_url == expected_url and expected_text == text_from_element

    @allure.description('Проверяем header на главной странице')
    @allure.title('Проверка главной страницы в разрешении 1920х1080')
    @pytest.mark.parametrize('page_driver', ['1920'], indirect=True)
    @pytest.mark.parametrize('locator,expected_url,exp_locator,expected_text,resolution', [
        [ABOUT_US_LOCATOR, PAGE_URL + ABOUT_US_LINK, ABOUT_US_TEXT_LOCATOR, ABOUT_EXPECTED_TEXT, 1],
        [SERVISES_LOCATOR, PAGE_URL + SERVISES_LINK, SERVICE_TEXT_LOCATOR, SERVICE_EXECTED_TEXT, 1],
        [REVIEWS_LOCATOR, PAGE_URL + REVIEWS_LINK, REVIEWS_TEXT_LOCATOR, REVIEWS_EXPECTED_TEXT, 1],
        [CONTACTS_LOCATOR, PAGE_URL + CONTACTS_LINK, CONTACTS_TEXT_LOCATOR, CONTACTS_EXPECTED_TEXT, 1],
        [SPECIALIST_LOCATOR, PAGE_URL + SPECIALIST_LINK, SPECIALIST_TEXT_LOCATOR, SPECIALIST_EXPECTED_TEXT, 1]
    ])
    def test_check_main_window_1920_1080(self, page_driver, locator, expected_url, exp_locator, expected_text,
                                         resolution):
        main_page = MainPage(page_driver)
        locator = main_page.modify_locator(locator, resolution)
        main_page.wait_element_on_page(locator)
        main_page.click_on_link(locator)
        page_url = main_page.get_url()
        main_page.wait_element_on_page(exp_locator)
        text_from_element = main_page.get_element_text(exp_locator)
        assert page_url == expected_url and expected_text == text_from_element
