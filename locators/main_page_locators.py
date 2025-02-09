from selenium.webdriver.common.by import By

MENU_LOCATOR = By.XPATH,'//*[@class="t-menuburger t-menuburger_first t-menuburger__small"]'

ABOUT_US_LOCATOR = By.XPATH,'//a[@class="{}"][@href="#about"]'
ABOUT_US_TEXT_LOCATOR = By.XPATH,'//*[@field="tn_text_1680508197689"]'

SERVISES_LOCATOR = By.XPATH,'//a[@class="{}"][@href="#moreinfo"]'
SERVICE_TEXT_LOCATOR = By.XPATH,'//*[@field="tn_text_1680510339492"]'

PROJECTS_LOCATOR = By.XPATH,'//a[@class="{}"][@href="#cases"]'
PROJECTS_TEXT_LOCATOR = By.XPATH,"//*[@field='tn_text_1680612130118']/span[text()='реализация приложения']"


REVIEWS_LOCATOR = By.XPATH,'//a[@class="{}"][@href="#Reviews"]'
REVIEWS_TEXT_LOCATOR = By.XPATH,'//*[@class="t-section__title t-title t-title_xs"]'


CONTACTS_LOCATOR = By.XPATH,'//a[@class="{}"][@href="#contacts"]'
CONTACTS_TEXT_LOCATOR = By.XPATH,'//*[@field="tn_text_1680515874720"]'

SPECIALIST_LOCATOR = By.XPATH,'//a[@class="{}"][@href="#specialists"]'
SPECIALIST_TEXT_LOCATOR = By.XPATH,'//*[text()="Наш стек"]'
