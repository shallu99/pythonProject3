import time
from datetime import datetime

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import logging
import os
import datetime
# from utils import parent_dir
# from utils.updateexcelfile import UpdateExcel as xl

logger = logging.getLogger(__name__)


class genlibA:

    def __init__(self, driver):
        self.driver = driver

    def launchbrowser(self, url, testcase):
        try:
            # with allure.step("launch the  browser"):

            driver = webdriver.Chrome("C:\\webdriver\\chromedriver_win32 (1)\\chromedriver.exe")
            driver.get(url)
            time.sleep(4)
            self.driver.get_screenshot_as_file("screenshot.png")
            allure.attach.file("screenshot.png", name="actual tittle ",attachment_type=allure.attachment_type.PNG)

            #
                # act_title = self.driver.title
                # print(act_title)
                #
                # if act_title == "OrangeHRM123":
                #     # try:
                #     #     self.driver.get_screenshot_as_file("screenshot.png")
                #     # except Exception as e:
                #     #     print(f"Error capturing screenshot: {str(e)}")
                #
                #     self.driver.get_screenshot_as_file("screenshot.png")
                #     allure.attach.file("screenshot.png", name="actual tittle ",
                #                        attachment_type=allure.attachment_type.PNG)
                #     assert True
                # else:
                #
                #     self.driver.get_screenshot_as_file("screenshot.png")
                #     allure.attach.file("screenshot.png", name="actual tittle ",
                #                        attachment_type=allure.attachment_type.PNG)
                #
                #     assert False
                # driver.get_screenshot_as_file("screenshot.png")
                # allure.attach.file("screenshot.png", name="password input ", attachment_type=allure.attachment_type.JPG)

            #self.driver.maximize_window()
            # self.updatesteps(testcase, "Launched the Browser and Navigated to the " + url + " URL successfully", "PASSED","")
        #     print(f"launched the URL successfully :  {url}")
        #     return True
        # except Exception as e:
        #     logger.error(f"Failed to lunch the url : {url}, error: {e}")
            # parentdirecotry = parent_dir.parent_dir()
            # now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            # screenshot_name = f"URL_{now}_screenshot.jpg"
            # screenshot_path = os.path.join(parentdirecotry, "RantCell_V1\\screenshots", screenshot_name)
            # self.driver.save_screenshot(screenshot_path)
            # xl.updatesteps(testcase, "Failed to launch the browser " + url, "FAILED",screenshot_path)

        except Exception as error:
            print(error)





