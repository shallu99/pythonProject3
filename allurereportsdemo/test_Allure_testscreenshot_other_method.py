import base64
from datetime import time
import time
import allure
from allure_commons.types import AttachmentType
from allure import attachment_type
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from programs.conftest import driver


class TestLogin():

    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self):
        try:
            self.driver = webdriver.Chrome("C:\\webdriver\\chromedriver_win32 (1)\\chromedriver.exe")
            self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
            self.driver.maximize_window()
            time.sleep(2)
            # screenshot = cls.driver.get_screenshot_as_png()
            png_data = self.driver.get_screenshot_as_png()
            filename = "screenshot.png"
            with open(filename, 'wb') as f:
                f.write(png_data)
            with open(filename, 'rb') as f:
                png_base64 = base64.b64encode(f.read()).decode('utf-8')
            os.remove(filename)

            # png_data = self.driver.get_screenshot_as_png()
            # png_base64 = base64.b64encode(png_data).decode('utf-8')
            allure.attach.file(png_base64, name='screenshot', attachment_type=allure.attachment_type.PNG)
            # Take a screenshot of the Login page and attach it to the allure report
            username_input = self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys("Admin")

            png_data = self.driver.get_screenshot_as_png()
            filename = "screenshot.png"
            with open(filename, 'wb') as f:
                f.write(png_data)
            with open(filename, 'rb') as f:
                png_base64 = base64.b64encode(f.read()).decode('utf-8')
            os.remove(filename)

            allure.attach.file(png_base64, name='screenshot', attachment_type=allure.attachment_type.PNG)
            password_input = self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys("admin123")
            png_data = self.driver.get_screenshot_as_png()
            filename = "screenshot.png"
            with open(filename, 'wb') as f:
                f.write(png_data)
            with open(filename, 'rb') as f:
                png_base64 = base64.b64encode(f.read()).decode('utf-8')
            os.remove(filename)

            allure.attach.file(png_base64, name='screenshot', attachment_type=allure.attachment_type.PNG)
            # Take a screenshot after entering the password and attach it to the allure report

            login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
            png_data = self.driver.get_screenshot_as_png()
            png_base64 = base64.b64encode(png_data).decode('utf-8')

            # screenshot = cls.driver.get_screenshot_as_png()
            allure.attach.file(png_base64, name='screenshot', attachment_type=allure.attachment_type.PNG)
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
