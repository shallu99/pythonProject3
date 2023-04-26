from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
import os
import datetime

# driver = None
logger = logging.getLogger(__name__)
def _capture_screenshot(driver,name):
    print(name)
    driver.get_screenshot_as_file(name)
def verifyElementispresent(driver,ByLocators,element,elementName):
    try:
        Element = driver.find_element(ByLocators,element)
        # Verify if the element is present
        if Element:
            logger.info(f"Element with id '{elementName,element}' is present on the page")
            now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            screenshot_name = f"{elementName}_{now}_screenshot.png"
            screenshot_path = os.path.join(os.getcwd(), "screenshots", screenshot_name)
            # _capture_screenshot(Element, screenshot_path)
            # Element.save_screenshot(screenshot_path)
            Element.screenshot(screenshot_path)
            return True
    except:
        logger.error(f"Element with id '{elementName,element}' is not present on the page")
        now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_name = f"{elementName}_{now}_screenshot.png"
        screenshot_path = os.path.join(os.getcwd(), "screenshots", screenshot_name)
        # _capture_screenshot(driver, screenshot_path)
        # driver.save_screenshot(screenshot_path)
        Element.screenshot(screenshot_path)
        return False



def verifyElementisVisible(driver,ByLocators,element,elementName):
    try:
        Element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((ByLocators, element)))
        if Element:
            logger.info(f"Element with id '{elementName,element}' is visible on the page")
            now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            screenshot_name = f"{elementName}_{now}_screenshot.png"
            screenshot_path = os.path.join(os.getcwd(), "screenshots", screenshot_name)
            # _capture_screenshot(driver, screenshot_path)
            # driver.save_screenshot(screenshot_path)
            Element.screenshot(screenshot_path)
            return True
    except:
        logger.error(f"Element with id '{elementName}' is not visible on the page")
        now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_name = f"{elementName}_{now}_screenshot.png"
        screenshot_path = os.path.join(os.getcwd(), "screenshots", screenshot_name)
        # _capture_screenshot(driver, screenshot_path)
        # driver.save_screenshot(screenshot_path)
        Element.screenshot(screenshot_path)
        return False

def verifyElementString(driver,ByLocators,element,elementName, expected_text):
    try:
        Element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((ByLocators, element)))
        actual_text = element.text.strip()
        assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"
        logger.info(f"Element with id '{elementName,element}' has the expected text '{expected_text}'")
        now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_name = f"{elementName}_{now}_screenshot.png"
        screenshot_path = os.path.join(os.getcwd(), "screenshots", screenshot_name)
        # _capture_screenshot(driver, screenshot_path)
        # driver.save_screenshot(screenshot_path)
        Element.screenshot(screenshot_path)
        return True
    except Exception as e:
        logger.error(f"Element with id '{elementName,element}' does not have the expected text '{expected_text}': {str(e)}")
        now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_name = f"{elementName}_{now}_screenshot.png"
        screenshot_path = os.path.join(os.getcwd(), "screenshots", screenshot_name)
        # _capture_screenshot(driver, screenshot_path)
        # driver.save_screenshot(screenshot_path)
        Element.screenshot(screenshot_path)
        return False