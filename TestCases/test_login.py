import pytest
from selenium import webdriver
from Pageobject.LoginPage import loginPage
from Utilities.ReadProperties import Readconfig
from Utilities.CustomLogger import LogGen


class Test_001_login:
    baseURL=Readconfig.getApplication()
    username=Readconfig.getUsername()
    password=Readconfig.getPassword()
    logger=LogGen.loggen()


    @pytest.mark.regression
    def test_homePageTitle(self,setup):

        self.logger.info("**********************Test_001_login*********************")
        self.logger.info("**********************Verifying homePageTitle*********************")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**********************test_homePageTitle is passed*********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("**********************test_homePageTitle is failed*********************")
            assert False




    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=loginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False

