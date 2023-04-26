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
    @allure.severity(allure.severity_level.MINOR)
    def test_logo(self):
        # try:
        self.driver = webdriver.Chrome("C:\\webdriver\\chromedriver_win32 (1)\\chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()

        time.sleep(2)
        status = self.driver.find_element(By.XPATH, "//img[@alt='company-branding']").is_displayed()
        time.sleep(2)
        if status == True:
            self.driver.close()
            assert True
        else:
            self.driver.get_screenshot_as_file("screenshot.png")
            allure.attach.file("screenshot.png", name="password input ", attachment_type=allure.attachment_type.PNG)
            self.driver.close()
            assert False

    # except Exception as error:
    #     print(error)

    @allure.severity(allure.severity_level.NORMAL)
    def test_listemployees(self):
        pytest.skip('skipping test...Later I will implement...')

    @allure.severity(allure.severity_level.BLOCKER)
    def test_Login(self):
        try:
            self.driver = webdriver.Chrome("C:\\webdriver\\chromedriver_win32 (1)\\chromedriver.exe")
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            self.driver.maximize_window()
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            time.sleep(2)
            act_title=self.driver.title
            print(act_title)

            if act_title=="OrangeHRM123":
                # try:
                #     self.driver.get_screenshot_as_file("screenshot.png")
                # except Exception as e:
                #     print(f"Error capturing screenshot: {str(e)}")

                self.driver.close()
                assert True
            else:

                self.driver.get_screenshot_as_file("screenshot.png")
                allure.attach.file("screenshot.png", name="password input ", attachment_type=allure.attachment_type.PNG)
                self.driver.close()
                assert False
        except Exception as error:
            print(error)
            assert False
        # finally:
        #     allure.attach.file("screenshot.png", name="logintest", attachment_type=AttachmentType.PNG)
