import os
from datetime import datetime

import allure
from allure_commons.types import AttachmentType

# def takescreenshot(driver, step_name):
#     allure.attach(driver.get_screenshot_as_png(), name=step_name, attachment_type=AttachmentType.PNG)

# [working alluere screenshot at each step]



def screenshotforurl(driver):
   
    driver.get_screenshot_as_file("screenshot.png")
    allure.attach.file("screenshot.png", name="password input ", attachment_type=allure.attachment_type.JPG)



