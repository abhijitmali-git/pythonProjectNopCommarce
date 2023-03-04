import time
import pytest
from Pageobject.LoginPage import loginPage
from Pageobject.AddCustomer import AddCustomer
from Pageobject.SearchCustomerPage import SearchCustomer
from Utilities.ReadProperties import Readconfig
from Utilities.CustomLogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseURL = Readconfig.getApplication()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("*************Test_SearchCustomerByEmail_004**************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=loginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("**************Login Sucessful**********************")
        time.sleep(3)

        self.logger.info("***************Starting search Customer By Email*******************")

        self.addcust=AddCustomer(self.driver)
        self.addcust.ClickOnCustomerMenu()
        self.addcust.ClickOnCustomerManuitem()
        self.logger.info("********************Searching Customer By email Id******************")
        searchcust=SearchCustomer(self.driver)
        searchcust.SetEmail("abhijitmali605@gmail.com")
        searchcust.ClickSearch()
        time.sleep(5)
        status=searchcust.searchCustomerByEmail("abhijitmali605@gmail.com")
        assert True==status
        self.logger.info("*******************TC_SearchCustomerByEmail_004 Finished**********************")
        self.driver.close()

