import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# from pytestframework.conftest import driver
from Utilities import exceltable
# from utilis.TestData import Data
from Utilities.verification  import *
# from utilis.Verification import click
from Utilities import genutils


# from pytestframework.conftest import *

class TestClass():

    @pytest.mark.parametrize("Password,DEVICES,Environment,URL,Login,CAMPAIGNS,Types_of_Test",
                             [(data["Password"], data["DEVICES"], data["Environment"], data["URL"], data["Login"],
                               data["CAMPAIGNS"], data['Types of Test']) for data in
                              exceltable.exceltables().readExcelSheetcombinations('T001')])
    def test_login_functionality(self, driver, Password, DEVICES, Environment, URL, Login, CAMPAIGNS, Types_of_Test):
        try:
            login_button = (By.ID, "loginbutton")
            Email_TextBox = (By.ID, "email")
            Password_TextBox = (By.ID, "password")
            print("URL: ", URL)
            driver.get(URL)
            driver.implicitly_wait(10)
            driver.find_element(By.ID, "email").send_keys(Login)
            verifyElementispresent(driver, Email_TextBox, 'Email_TextBox')
            # verifyElementString(self.driver,self.login_button,'login',"Login_Button")
            time.sleep(2)
            driver.find_element(By.ID, "password").send_keys(Password)
            # verifyElementisVisible(self.driver,(self.Password_TextBox),"Password_Textbox")
            time.sleep(2)
            genutils.click(driver, login_button)
            # self.driver.find_element(By.ID, "loginbutton").click()

            # TestClass().click(self.driver,self.login_button)
            time.sleep(2)
            assert driver.title == "RantCell | Dashboard"
            # time.sleep(2)
            # self.driver.find_element(By.XPATH,'//*[@id="mapView"]/div[1]/div/a[1]/i').click()
            #
            # xpath = "//*[text()[contains(.,'"+Types_of_Test+"')]]"
            # time.sleep(2)
            # self.driver.find_element(By.XPATH, xpath).click()
            # time.sleep(2)
        except Exception as e:
            pytest.fail(f"Test case failed on iteration : {str(e)}")