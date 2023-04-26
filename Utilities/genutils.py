from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def click(driver, locator):
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()
        print(f"Clicked on element with locator: {locator}")
    except Exception as e:
        print(f"Failed to click on element with locator: {locator, e}")