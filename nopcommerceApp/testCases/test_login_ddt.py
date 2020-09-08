import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import ExcelUtils
import time

class Test_002_DDT_Login:
    baseURL = "https://hr-kernet-dev.firebaseapp.com/auth/login"
    path=".//TestData/LoginData.xlsx"
    logger=LogGen.logged()

    def test_login_ddt(self,setup):
        self.logger.info("************Test_002_DDT_Login***********")
        self.logger.info("************Verify Login DDT Test***********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in an Excel file:", self.rows)
        lst_status=[]       #Empty List variable

        for r in range(2, self.rows+1):
            self.email = ExcelUtils.readData(self.path, 'Sheet1',r,1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1',r,2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1',r,3)

            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickSignIn()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Recruit"

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("**** Passed")
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("**** Failed")
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("**** Failed")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("*** Passed ***")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("**** Login DDT Test Passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Login DDT Test Failed ****")
            self.driver.close()
            assert False

        self.logger.info("*************** End of Login DDT Test **************")
        self.logger.info("*************** Completed TC_LoginDDT_002 **************")