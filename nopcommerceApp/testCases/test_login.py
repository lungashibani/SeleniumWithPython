import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = "https://hr-kernet-dev.firebaseapp.com/auth/login"
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()

    logger=LogGen.logged()

    def test_homePageTitle(self,setup):

        self.logger.info("************Test_001_Login***********")
        self.logger.info("************Verify Home Page Title***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Recruit":
            assert True
            self.driver.close()
            self.logger.info("************Home Page Title Has Passed***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************Home Page Title Has Failed***********")
            assert False

    def test_login(self,setup):
        self.logger.info("************Verify Login Test***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickSignIn()
        act_title = self.driver.title
        if act_title == "Recruit":
            assert True
            self.logger.info("************Home Page Title Has Passed***********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("************Home Page Title Has Failed***********")
            assert False





