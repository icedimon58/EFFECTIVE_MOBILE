import pytest
from selenium import webdriver
from data import PAGE_URL


@pytest.fixture()
def page_driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument('window-size={},1080'.format(request.param))
    driver = webdriver.Chrome(options=options)
    driver.get(PAGE_URL)
    yield driver
    driver.quit()
