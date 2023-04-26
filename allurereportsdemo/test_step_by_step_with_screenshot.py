from requests import session
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
import pytest
import time


from Utilities import Allure_screenshot
from allurereportsdemo.functions import delete_reports
from allurereportsdemo.functions import generate_report

@pytest.fixture()
def browser():
    # delete_reports.delete()

    time.sleep(3)
    driver = webdriver.Chrome("C:\\webdriver\\chromedriver_win32 (1)\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.severity(allure.severity_level.NORMAL)
class TestHRM:

    @allure.title("Google search for 'OrangeHRM'")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_Login(self, browser):

        with allure.step("Navigate to URL"):
            browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            Allure_screenshot.screenshotforurl(browser)
            time.sleep(2)

        with allure.step("input the user login credential"):
            username_input = browser.find_element(By.XPATH, "//input[@name='username']")
            username_input.send_keys("Admin")
            Allure_screenshot.screenshotforurl(browser)
            time.sleep(2)

        with allure.step("input the user password credential"):
            password_input = browser.find_element(By.XPATH, "//input[@name='password']")
            password_input.send_keys("admin123")
            Allure_screenshot.screenshotforurl(browser)
            time.sleep(2)
        # generate_report.sessionfinish()


        # with allure.step("click login button"):
        #     login_btn = browser.find_element(By.XPATH, "//button[@type='submit']")
        #     login_btn.click()
        #     time.sleep(2)
        #
        # act_title = browser.title
        # print(act_title)
        #
        # if act_title == "OrangeHRM":
        #     Allure_screenshot.screenshotforurl(browser)
        #     assert True
        # else:
        #     assert False
