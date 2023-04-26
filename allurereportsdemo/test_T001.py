import time

import pytest

from allurereportsdemo.genlib.Keywords import genlibA

import allure
from selenium import webdriver

data = ["https://opensource-demo.orangehrmlive.com/web/index.php/auth/login","https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"]
class Test_T001:

    @pytest.mark.parametrize("url",data)
    def test_Login(self, url):

        genlibA.launchbrowser(self,url,"testcase")
