import os

import pytest
from selenium import webdriver
from data import PAGE_URL

@pytest.fixture()
def page_driver(request):
    chrome_options = webdriver.ChromeOptions()
    if os.getenv('IS_DOCKER'):
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
    else:
        chrome_options.add_argument('window-size={},1080'.format(request.param))
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(PAGE_URL)
    yield driver
    driver.quit()
