import time

import self
from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import unittest
import pytest
from selenium.webdriver.common.by import By

@allure.severity(allure.severity_level.NORMAL)

class TestHRM:
    # driver = None
    # @allure.severity(allure.severity_level.MINOR)
    # def test_logo(self):
    #     # try:
    #     self.driver = webdriver.Chrome("C:\\webdriver\\chromedriver_win32 (1)\\chromedriver.exe")
    #     self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    #     self.driver.maximize_window()
    #
    #     time.sleep(2)
    #     status = self.driver.find_element(By.XPATH, "//img[alt='company-branding']").is_displayed()
    #     time.sleep(2)
    #     if status == True:
    #         assert True
    #     else:
    #
    #         self.driver.close()
    #         assert False
    #
    # # except Exception as error:
    # #     print(error)
    #
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_listemployees(self):
    #     pytest.skip('skipping test...Later I will implement...')

    @allure.severity(allure.severity_level.BLOCKER)
    def test_Login(self):
        try:
            self.driver = webdriver.Chrome("C:\\webdriver\\chromedriver_win32 (1)\\chromedriver.exe")
            # with open("screenshot.png", "rb") as file:

            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            self.driver.maximize_window()
            time.sleep(2)
            self.driver.get_screenshot_as_file("screenshot.png")
            allure.attach.file("screenshot.png", name="urlscreenshot", attachment_type=allure.attachment_type.PNG)

            self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
            self.driver.get_screenshot_as_file("screenshot.png")
            allure.attach.file("screenshot.png", name="Admin input ", attachment_type=allure.attachment_type.PNG)
            # with open("screenshot.png", "rb") as file:
            #     screenshot = file.read()
            # allure.attach(screenshot, name="Screenshot", attachment_type=allure.attachment_type.PNG)
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
            self.driver.get_screenshot_as_file("screenshot.png")
            allure.attach.file("screenshot.png", name="password input ", attachment_type=allure.attachment_type.PNG)
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

            time.sleep(2)
            act_title = self.driver.title
            print(act_title)

            if act_title == "OrangeHRM":
                self.driver.get_screenshot_as_file("screenshot.png")
                allure.attach.file("screenshot.png", name="tittle verify", attachment_type=allure.attachment_type.PNG)

                # self.driver.close()
                assert True
            else:

                # self.driver.close()
                assert False
        except Exception as error:
            print(error)
            # assert False
            self.driver.quit()


# this is the expected code for each step screenshot