
import pytest
from selenium import webdriver
from data import PAGE_URL


@pytest.fixture
def page_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('window-size=1920,1080')
    options.add_argument('--headless')
    options.add_argument('no-sandbox')
    # options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.get(PAGE_URL)
    yield driver
    driver.quit()

