import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AddCustomer:
    lnkCustomers_manu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_Addnew_xpath="//a[@class='btn btn-primary']"
    txtEmail_id="Email"
    txtPassword_id="Password"
    txt_Firstname_id="FirstName"
    txt_Lastname_id="LastName"
    rdMaleGender_id="Gender_Male"
    rdFemaleGender_id="Gender_Female"
    txtDob_id="DateOfBirth"
    txtCompanyname_id="Company"
    ckbIsTaxExempt_id="IsTaxExempt"
    drpNewslatter_xpath="//div[@class='input-group-append']//div[@role='listbox']"
    lstitemCustomersRoles_xpath="//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lstitemRegistered_xpath="//span[normalize-space()='Registered']"
    lstitemAdministrator_xpath="//span[normalize-space()='Administrators']"
    lstitemGuest_xpath="//span[normalize-space()='Guests']"
    lstitemForumModerators_xpath="//span[normalize-space()='Forum Moderators']"
    lstitemVendors_xpath="//span[normalize-space()='Vendors']"
    drpitemMngrofVendors="//select[@id='VendorId']"
    txtAdminContext_xpath="//textarea[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def ClickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_manu_xpath).click()

    def ClickOnCustomerManuitem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()

    def ClickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.btn_Addnew_xpath).click()

    def SetEmail(self,email):
        self.driver.find_element(By.ID,self.txtEmail_id).send_keys(email)

    def SetPassword(self,password):
        self.driver.find_element(By.ID,self.txtPassword_id).send_keys(password)

    time.sleep(3)

    def SetFirstname(self,fname):
        self.driver.find_element(By.ID,self.txt_Firstname_id).send_keys(fname)
    def SetLastname(self,lname):
        self.driver.find_element(By.ID,self.txt_Lastname_id).send_keys(lname)

    def SetGender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender=="Female":
            self.driver.find_element(By.ID,self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()

    def SetDob(self,dob):
        self.driver.find_element(By.ID,self.txtDob_id).send_keys(dob)
    def Companyname(self,cname):
        self.driver.find_element(By.ID,self.txtCompanyname_id).send_keys(cname)

    def ClickOnIsTaxExempt(self):
        self.driver.find_element(By.ID,self.ckbIsTaxExempt_id).click()

    def ClickOnNewsLatter(self):
        drp_element=(self.driver.find_element(By.XPATH,self.drpNewslatter_xpath))
        drp_newslatter=Select(drp_element)
        drp_newslatter.select_by_index(0)

    def SetCustomerRole(self,role):
        self.driver.find_element(By.XPATH,self.lstitemCustomersRoles_xpath).click()
        time.sleep(3)
        if role=='Registered':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role=='Administrators':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemAdministrator_xpath)
        elif role=='Guests':
            # here user can be registered or guest only one
            self.driver.find_element(By.XPATH,"//span[@title='delete']").click()
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemGuest_xpath)
        elif role=='Registered':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role=='Vendors':
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)
        else:
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemGuest_xpath)
        time.sleep(3)
        self.listitem.click()
        #self.driver.execute_script("argument[0].click();",self.listitem)

    def ClickOnManagerOfVendor(self,value):
        drp_element=(self.driver.find_element(By.XPATH,self.drpitemMngrofVendors))
        drp_manager=Select(drp_element)
        drp_manager.select_by_visible_text(value)

    def ClickOnAdminContext(self,content):
        self.driver.find_element(By.XPATH,self.txtAdminContext_xpath).send_keys(content)

    def ClickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()





