
import pytest
from selenium import webdriver
from data import PAGE_URL


@pytest.fixture
def page_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.get(PAGE_URL)
    yield driver
    driver.quit()

