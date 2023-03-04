from selenium.webdriver.common.by import By
class SearchCustomer:
    txtEmail_id="SearchEmail"
    txtFname_id="SearchFirstName"
    txtLname_id="SearchLastName"
    btnSearch_id="search-customers"

    table_xpath="//table[@id='customers-grid']"
    tableRows_xpath="//table[@id='customers-grid']//tbody/tr"
    tableColumn_xpath="//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver=driver

    def SetEmail(self,email):
        self.driver.find_element(By.ID,self.txtEmail_id).clear()
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def SetFirstName(self,fname):
        self.driver.find_element(By.ID,self.txtFname_id).clear()
        self.driver.find_element(By.ID, self.txtFname_id).send_keys(fname)

    def SetLastName(self,lname):
        self.driver.find_element(By.ID,self.txtLname_id).clear()
        self.driver.find_element(By.ID, self.txtLname_id).send_keys(lname)

    def ClickSearch(self):
        self.driver.find_element(By.ID,self.btnSearch_id).click()


    def GetNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH,self.tableRows_xpath))

    def GetNoOfColumn(self):
        return len(self.driver.find_elements(By.XPATH,self.tableColumn_xpath))

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.GetNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            emailid=table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if emailid==email:
                flag=True
                break
        return flag

    def searchCustomerByName(self,name):
        flag=False
        for r in range(1,self.GetNoOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_xpath)
            Name=table.find_element(By.XPATH,"//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if Name==name:
                flag=True
                break
        return flag


