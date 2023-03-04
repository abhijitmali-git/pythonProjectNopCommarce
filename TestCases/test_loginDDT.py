import time

import pytest
from selenium import webdriver
from Pageobject.LoginPage import loginPage
from Utilities.ReadProperties import Readconfig
from Utilities.CustomLogger import LogGen
from Utilities import Exelutiles


class Test_001_DDT_login:
    baseURL=Readconfig.getApplication()
    path="TestData/TestData_login.xlsx"
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_login(self,setup):

        self.driver=setup
        self.driver.get(self.baseURL)

        self.lp=loginPage(self.driver)
        self.rows=Exelutiles.getRowcount(self.path,"Sheet1")
        print("No. of rows in exel",self.rows)
        status=[]
        for r in range(2,self.rows+1):
            self.user=Exelutiles.readDate(self.path,'Sheet1',r,1)
            self.password = Exelutiles.readDate(self.path, 'Sheet1', r, 2)
            self.exp = Exelutiles.readDate(self.path, 'Sheet1', r, 3)
            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=='Pass':
                    self.logger.info("****Pass****")
                    self.lp.clicklogout()
                    status.append("pass")
                elif self.exp=="Fail":
                    self.logger.info("*****Failed********")
                    self.lp.clicklogout()
                    status.append("Fail")
            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("******Failed********")
                    status.append('Fail')
                elif self.exp=="Fail":
                    self.logger.info("*******Pass*******")
                    status.append("Pass")


        if "Fail" not in status:
            self.logger.info("*********Logiin DDt test Passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("***********login DDT Test Failed")
            self.driver.close()
            assert False



