import random
import string
import pytest
from selenium.webdriver.common.by import By
from Utilities.ReadProperties import Readconfig
from Utilities.CustomLogger import LogGen
from Pageobject.LoginPage import loginPage
from Pageobject.AddCustomer import AddCustomer

class Test_003_AddCustomer:
    baseURL = Readconfig.getApplication()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("************Test_003_AddCustomer***********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=loginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("******Login Sucessful******")

        self.logger.info("***********Started Add Customer Test********")

        self.addcust=AddCustomer(self.driver)
        self.addcust.ClickOnCustomerMenu()
        self.addcust.ClickOnCustomerManuitem()
        self.addcust.ClickOnAddNew()
        self.logger.info("***********Providing Customer Info**************")

        self.Email=RandomGenerator()+ "@gmail.com"
        self.addcust.SetEmail(self.Email)
        self.addcust.SetPassword("test123")
        # self.addcust.ClickOnNewsLatter()
        #self.addcust.SetCustomerRole("Guests")
        #self.addcust.ClickOnManagerOfVendor("Vendor 2")
        self.addcust.ClickOnAdminContext("This is for Testing")
        self.addcust.SetFirstname("Abhi")
        self.addcust.SetLastname("Mali")
        self.addcust.SetGender("Male")
        self.addcust.SetDob("3/25/2000")
        self.addcust.Companyname("TCS")
        self.addcust.ClickOnIsTaxExempt()
        self.addcust.ClickOnSave()

        self.logger.info("**************Saving Customer Info***********")

        self.logger.info("***************Add Customer Validation Started*************")

        self.msg=self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        if "The new customer has been added successfully." in self.msg:
            assert True==True
            self.logger.info("**********AddCustomer Test Passed**************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer_scr.png")
            self.logger.info("**********Add Customer Test Failed*************")
            assert True == False

        self.driver.close()
        self.logger.info("***********Ending Add Test Customer Test*************")



def RandomGenerator(size=8, chars=string.ascii_lowercase + string.digits):
            return ''.join(random.choice(chars) for x in range(size))

