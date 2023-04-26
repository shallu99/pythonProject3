
from datetime import time
import time
import allure
from allure_commons.types import AttachmentType
from allure import attachment_type
from selenium import webdriver
from selenium.webdriver.common.by import By

from programs.conftest import driver


class TestLogin():

    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self):
        try:
            self.driver = webdriver.Chrome("C:\\webdriver\\chromedriver_win32 (1)\\chromedriver.exe")
            # screenshot = cls.driver.get_screenshot_as_png()
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            self.driver.maximize_window()
            time.sleep(2)

            allure.attach('screenshot', self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
            # Take a screenshot of the Login page and attach it to the allure report

            username_input = self.driver.find_element(By.XPATH, "//input[@name='username']")
            # screenshot = cls.driver.get_screenshot_as_png()
            username_input.send_keys("Admin")
            allure.attach('screenshot', self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
            # Take a screenshot after entering the username and attach it to the allure report

            password_input = self.driver.find_element(By.XPATH, "//input[@name='password']")
            # screenshot = cls.driver.get_screenshot_as_png()
            password_input.send_keys("admin123")

            allure.attach('screenshot', self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
            # Take a screenshot after entering the password and attach it to the allure report

            login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            # screenshot = cls.driver.get_screenshot_as_png()
            login_button.click()

            allure.attach('screenshot', self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG)
            time.sleep(2)
            act_title = self.driver.title
            print(act_title)

            if act_title == "OrangeHRM":
                self.driver.close()
                assert True
            else:
                self.driver.close()
                assert False
        except Exception as error:
            print(error)
            assert False
# if __name__ == '__main__':
#     unittest.main()
