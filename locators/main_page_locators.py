from selenium.webdriver.common.by import By

from data import HEADERS_LINK

ABOUT_US_LOCATOR = By.XPATH,HEADERS_LINK+'[@href="#about"]'
ABOUT_US_TEXT_LOCATOR = By.XPATH,'//*[@field="tn_text_1680508197689"]'

SERVISES_LOCATOR = By.XPATH,HEADERS_LINK+'[@href="#moreinfo"]'
SERVICE_TEXT_LOCATOR = By.XPATH,'//*[@field="tn_text_1680510339492"]'

PROJECTS_LOCATOR = By.XPATH,HEADERS_LINK+'[@href="#cases"]'
PROJECTS_TEXT_LOCATOR = By.XPATH,'//*[@data-lid="1496797390759"]'
# PROJECTS_TEXT_LOCATOR = By.XPATH,'//*[@class="t396__elem tn-elem tn-elem__5731196821680612160870"]//div[@field="tn_text_1680612160870"]'
# //*[@id="rec573119682"]/div/div/div[9]/div/text()[1]
# PROJECTS_TEXT_LOCATOR = By.XPATH,'//*[@id="rec573119682"]/div/div/div[9]/div/text()[1]'
# //body/a[text()[contains(.,'Использовать новый стек технологий, для')]]

# //div[text()[contains(.,'Использовать новый стек технологий, для')]]

REVIEWS_LOCATOR = By.XPATH,HEADERS_LINK+'[@href="#Reviews"]'
REVIEWS_TEXT_LOCATOR = By.XPATH,'//*[@class="t-section__title t-title t-title_xs"]'




CONTACTS_LOCATOR = By.XPATH,HEADERS_LINK+'[@href="#contacts"]'
CONTACTS_TEXT_LOCATOR = By.XPATH,'//*[@field="tn_text_1680515874720"]'

SPECIALIST_LOCATOR = By.XPATH,HEADERS_LINK+'[@href="#specialists"]'
SPECIALIST_TEXT_LOCATOR = By.XPATH,'//*[text()="Наш стек"]'
#specialists


# MAIN_TEXT_LOCATOR = By.XPATH,"//*[text()='Высококвалифицированные специалисты или целая команда под ваши задачи']"



# CONTAKTS_LOCATOR = By.XPATH,"//*[text()='Контакты']"


