import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.login import LoginPage


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.saucedemo.com/')
    driver.implicitly_wait(10)
    request.cls.driver = driver
    request.cls.login_page = LoginPage(driver)
    before_failed = request.session.testsfailed
    yield
    # if request.session.testsfailed != before_failed:
    #     allure.attach(driver.get_screenshot_as_png(), name='Test failed', attachment_type=AttachmentType.PNG)
    driver.quit()

