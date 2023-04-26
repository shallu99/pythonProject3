import logger as logger
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import logging
import os
import datetime
# create a file handler
log_file = os.path.join(os.getcwd(), "logs", "my_log.log")
fh = logging.FileHandler(log_file)
fh.setLevel(logging.INFO)

# create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# # add the handler to the logger
# logger.addHandler(fh)
# driver = None
logger = logging.getLogger(__name__)

def _capture_screenshot(driver,name):
    print(name)
    driver.get_screenshot_as_file(name)
def verifyElementispresent(driver,Locators,elementName):

        outcome = yield
        report = outcome.get_result()
        if report.when == 'call' and not report.skipped:
            try:
                LocatorsType = Locators[0]
                PropertyValue = Locators[1]
                Element = driver.find_element(LocatorsType,PropertyValue)
                # Verify if the element is present
                if Element:
                    log_message= logger.info(f"Element with id '{elementName,Locators}' is present on the page")
                    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                    screenshot_name = f"{elementName}_{now}_screenshot.png"
                    cwd = os.getcwd()
                    screenshot_path = os.path.join(cwd, "screenshots", screenshot_name)
                    print("os ",os.getcwdb())
                    # _capture_screenshot(Element, screenshot_path)
                    # Element.save_screenshot(screenshot_path)
                    Element.screenshot(screenshot_path)
                    with open(screenshot_path, 'rb') as f:
                        screenshot_data = f.read()
                    report.extra.append(pytest_html.extras.image(screenshot_data, screenshot_name))
                    logger.info(log_message)
                    return True
            except:
                log_message = logger.error(f"Element with id '{elementName,Locators}' is not present on the page")
                now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                screenshot_name = f"{elementName}_{now}_screenshot.png"
                cwd = os.getcwd()
                screenshot_path = os.path.join(cwd, "screenshots", screenshot_name)
                # _capture_screenshot(driver, screenshot_path)
                # driver.save_screenshot(screenshot_path)
                Element.screenshot(screenshot_path)
                with open(screenshot_path, 'rb') as f:
                    screenshot_data = f.read()
                report.extra.append(pytest_html.extras.image(screenshot_data, screenshot_name))
                logger.error(log_message)
                return False


@pytest.mark.hookwrapper
def verifyElementisVisible(driver,Locators,elementName):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and not report.skipped:
        try:
            Element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators))
            if Element:
                log_message =logger.info(f"Element with id '{elementName,Locators}' is visible on the page")
                now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                screenshot_name = f"{elementName}_{now}_screenshot.png"
                screenshot_path = os.path.join(os.getcwd(), "screenshots", screenshot_name)
                # _capture_screenshot(driver, screenshot_path)
                # driver.save_screenshot(screenshot_path)
                Element.screenshot(screenshot_path)
                with open(screenshot_path, 'rb') as f:
                    screenshot_data = f.read()
                report.extra.append(pytest_html.extras.image(screenshot_data, screenshot_name))
                logger.info(log_message)
                return True
        except:
            log_message =logger.error(f"Element with id '{elementName,Locators}' is not visible on the page")
            now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            screenshot_name = f"{elementName}_{now}_screenshot.png"
            screenshot_path = os.path.join(os.getcwd(), "screenshots", screenshot_name)
            # _capture_screenshot(driver, screenshot_path)
            # Element.save_screenshot(screenshot_path)
            driver.screenshot(screenshot_path)
            with open(screenshot_path, 'rb') as f:
                screenshot_data = f.read()
            report.extra.append(pytest_html.extras.image(screenshot_data, screenshot_name))
            logger.error(log_message)
            return False

def verifyElementString(driver,Locators, expected_text,elementName):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and not report.skipped:
        try:
            Element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators))
            actual_text = Element.text.strip()
            assert actual_text == expected_text, f"Expected text '{expected_text}', but got '{actual_text}'"
            log_message =logger.info(f"Element with id '{elementName,Locators}' has the expected text '{expected_text}' and actual text '{actual_text}'")
            now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            screenshot_name = f"{elementName}_{now}_screenshot.png"
            screenshot_path = os.path.join(os.getcwd(), "screenshots", screenshot_name)
            # _capture_screenshot(driver, screenshot_path)
            # driver.save_screenshot(screenshot_path)
            Element.screenshot(screenshot_path)
            with open(screenshot_path, 'rb') as f:
                screenshot_data = f.read()
            report.extra.append(pytest_html.extras.image(screenshot_data, screenshot_name))
            logger.info(log_message)
            return True
        except Exception as e:
            log_message = logger.error(f"Element with id '{elementName,Locators}' does not have the expected text '{expected_text}': {str(e)} and actual text'{actual_text}' ")
            now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            screenshot_name = f"{elementName}_{now}_screenshot.png"
            screenshot_path = os.path.join(os.getcwd(), "screenshots", screenshot_name)
            # _capture_screenshot(driver, screenshot_path)
            # driver.save_screenshot(screenshot_path)
            Element.screenshot(screenshot_path)
            with open(screenshot_path, 'rb') as f:
                screenshot_data = f.read()
            report.extra.append(pytest_html.extras.image(screenshot_data, screenshot_name))
            logger.error(log_message)
            return False
