# Ricardo Parra
# Studen ID: 8808044

import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class FormTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
       
    # Test to create user in e-commerce portal
    def test_create_user_success(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")

        link_create = driver.find_element(By.PARTIAL_LINK_TEXT,"Create an Account")
        link_create.click()

        driver.implicitly_wait(2)

        firstname = driver.find_element(By.NAME, 'firstname')
        firstname.send_keys("Ricardo")

        lastname = driver.find_element(By.NAME, 'lastname')
        lastname.send_keys("Parra")

        email = driver.find_element(By.NAME, 'email')
        email.send_keys("testfinal@gmail.com")

        password = driver.find_element(By.NAME, 'password')
        password.send_keys("Websecurity2023")

        password_confirmation = driver.find_element(By.NAME, 'password_confirmation')
        password_confirmation.send_keys("Websecurity2023")

        button = driver.find_element(By.XPATH,"//button[@title='Create an Account']")
        button.click()
        
        driver.implicitly_wait(5)

        element2 = driver.find_element(By.XPATH,"//div[text()='Thank you for registering with Main Website Store.']")

        self.assertEqual("Thank you for registering with Main Website Store.", element2.text)
    
        # Print the text content
        print("Successful Test Create User!")       
        
        time.sleep(3)

    # Test to create user in e-commerce portal with password validation
    def test_create_user_password_validation(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")

        link_create = driver.find_element(By.PARTIAL_LINK_TEXT,"Create an Account")
        link_create.click()

        driver.implicitly_wait(2)

        firstname = driver.find_element(By.NAME, 'firstname')
        firstname.send_keys("Ricardo")

        lastname = driver.find_element(By.NAME, 'lastname')
        lastname.send_keys("Parra")

        email = driver.find_element(By.NAME, 'email')
        email.send_keys("testfinal@gmail.com")
        
        button = driver.find_element(By.XPATH,"//button[@title='Create an Account']")
        button.click()
        
        driver.implicitly_wait(5)
                
        password_error = driver.find_element(By.ID,'password-error')

        self.assertEqual("This is a required field.", password_error.text)

        print("Successful Test Create User with Password Validation!")       
        
        time.sleep(3)

    # Test to create user in e-commerce portal with length password validation
    def test_create_user_password_length_validation(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")

        link_create = driver.find_element(By.PARTIAL_LINK_TEXT,"Create an Account")
        link_create.click()

        driver.implicitly_wait(2)

        firstname = driver.find_element(By.NAME, 'firstname')
        firstname.send_keys("Ricardo")

        lastname = driver.find_element(By.NAME, 'lastname')
        lastname.send_keys("Parra")

        email = driver.find_element(By.NAME, 'email')
        email.send_keys("testfinal@gmail.com")

        password = driver.find_element(By.NAME, 'password')
        password.send_keys("Web")
        
        button = driver.find_element(By.XPATH,"//button[@title='Create an Account']")
        button.click()
        
        driver.implicitly_wait(5)
                
        password_error = driver.find_element(By.ID,'password-error')

        extracted_error = password_error.text[:69]

        self.assertEqual("Minimum length of this field must be equal or greater than 8 symbols.", extracted_error)

        print("Successful Test Create User with Length Password Validation!")       
        
        time.sleep(3)

    # Test to create user in e-commerce portal with length password validation
    def test_create_user_password_types_validation(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")

        link_create = driver.find_element(By.PARTIAL_LINK_TEXT,"Create an Account")
        link_create.click()

        driver.implicitly_wait(2)

        firstname = driver.find_element(By.NAME, 'firstname')
        firstname.send_keys("Ricardo")

        lastname = driver.find_element(By.NAME, 'lastname')
        lastname.send_keys("Parra")

        email = driver.find_element(By.NAME, 'email')
        email.send_keys("testfinal@gmail.com")

        password = driver.find_element(By.NAME, 'password')
        password.send_keys("Websecurity")
        
        button = driver.find_element(By.XPATH,"//button[@title='Create an Account']")
        button.click()
        
        driver.implicitly_wait(5)
                
        password_error = driver.find_element(By.ID,'password-error')

        extracted_error = password_error.text[:60]

        self.assertEqual("Minimum of different classes of characters in password is 3.", extracted_error)

        print("Successful Test Create User with Types Password Validation!")       
        
        time.sleep(3)

    # Test to create user in e-commerce portal with password confirmation same value
    def test_create_user_password_types_validation(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")

        link_create = driver.find_element(By.PARTIAL_LINK_TEXT,"Create an Account")
        link_create.click()

        driver.implicitly_wait(2)

        firstname = driver.find_element(By.NAME, 'firstname')
        firstname.send_keys("Ricardo")

        lastname = driver.find_element(By.NAME, 'lastname')
        lastname.send_keys("Parra")

        email = driver.find_element(By.NAME, 'email')
        email.send_keys("testfinal@gmail.com")

        password = driver.find_element(By.NAME, 'password')
        password.send_keys("Websecurity2023")

        password_confirmation = driver.find_element(By.NAME, 'password_confirmation')
        password_confirmation.send_keys("Websecurity")
        
        button = driver.find_element(By.XPATH,"//button[@title='Create an Account']")
        button.click()
        
        driver.implicitly_wait(5)
                
        password_confirmation_error = driver.find_element(By.ID,'password-confirmation-error')

        self.assertEqual("Please enter the same value again.", password_confirmation_error.text)

        print("Successful Test Create User with Password Confirmation Validation!")       
        
        time.sleep(3)

    # Test for login user - enter valid email address 
    def test_login_user_email_success(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")

        link_sign_in = driver.find_element(By.PARTIAL_LINK_TEXT,"Sign In")
        link_sign_in.click()

        login = driver.find_element(By.NAME, 'login[username]')
        login.send_keys("accountgmail.com")

        button = driver.find_element(By.ID,'send2')
        button.click()
        
        driver.implicitly_wait(5)

        email_error = driver.find_element(By.ID,'email-error')

        self.assertEqual("Please enter a valid email address (Ex: johndoe@domain.com).", email_error.text)
        
        print("Successful Test Login User with Email Validation!")       
        
        time.sleep(3)

    # Test for login user - password required 
    def test_login_user_email_success(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")

        link_sign_in = driver.find_element(By.PARTIAL_LINK_TEXT,"Sign In")
        link_sign_in.click()

        login = driver.find_element(By.NAME, 'login[username]')
        login.send_keys("test2@gmail.com")

        button = driver.find_element(By.ID,'send2')
        button.click()
        
        driver.implicitly_wait(5)

        password_error = driver.find_element(By.ID,'pass-error')

        self.assertEqual("This is a required field.", password_error.text)
        
        print("Successful Test Login User with Password Validation!")       
        
        time.sleep(3)

    # Test for login user 
    def test_login_user_success(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")

        link_sign_in = driver.find_element(By.PARTIAL_LINK_TEXT,"Sign In")
        link_sign_in.click()

        login = driver.find_element(By.NAME, 'login[username]')
        login.send_keys("tmp2@gmail.com")

        password = driver.find_element(By.NAME, 'login[password]')
        password.send_keys("Websecurity2023")
        
        button = driver.find_element(By.ID,'send2')
        button.click()
        
        driver.implicitly_wait(5)

        link_sign_out = driver.find_element(By.XPATH,"//a[contains(@href, '/customer/account/logout/')]")
        
        self.assertEqual("https://magento.softwaretestingboard.com/customer/account/logout/", link_sign_out.get_attribute("href"))
      
        print("Successful Test Login User!")       
        
        time.sleep(3)

    #Test for change password
    def test_change_password_success(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/customer/account/login/")

        link_login = driver.find_element(By.PARTIAL_LINK_TEXT,"Sign In")
        link_login.click()

        driver.implicitly_wait(2)

        login = driver.find_element(By.NAME, 'login[username]')
        login.send_keys("tmp2@gmail.com")

        password = driver.find_element(By.NAME, 'login[password]')
        password.send_keys("Websecurity2023")
        
        button = driver.find_element(By.ID,'send2')
        button.click()
        
        driver.implicitly_wait(3)

        change_password = driver.find_element(By.XPATH,"//a[contains(@class, 'action change-password') and contains(text(), 'Change Password')]")
        change_password.click()

        current_password = driver.find_element(By.NAME,'current_password')
        current_password.send_keys("Websecurity2023")

        password = driver.find_element(By.NAME,'password')
        password.send_keys("Websecurity2023")

        password_confirmation = driver.find_element(By.NAME,'password_confirmation')
        password_confirmation.send_keys("Websecurity2023")

        button_save = driver.find_element(By.XPATH,"//button[@title='Save']")
        button_save.click()

        driver.implicitly_wait(3)

        element = driver.find_element(By.XPATH,"//div[contains(text(), 'You saved the account information.')]")
        
        self.assertEqual("You saved the account information.", element.text)
      
        print("Successful Test Change Password!")        
        
        time.sleep(3)

    # Test Add New Address to user account
    def test_manage_address(self):

        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")

        link_sign_in = driver.find_element(By.PARTIAL_LINK_TEXT,"Sign In")
        link_sign_in.click()

        login = driver.find_element(By.NAME, 'login[username]')
        login.send_keys("tmp2@gmail.com")

        password = driver.find_element(By.NAME, 'login[password]')
        password.send_keys("Websecurity2023")
        
        button = driver.find_element(By.ID,'send2')
        button.click()

        driver.get("https://magento.softwaretestingboard.com/customer/address/new/")

        telephone = driver.find_element(By.NAME, 'telephone')
        telephone.send_keys("5199999999")

        street = driver.find_element(By.NAME, 'street[]')
        street.send_keys("Conestoga Doon")

        city = driver.find_element(By.NAME, 'city')
        city.send_keys("Kitchener")

        country = driver.find_element(By.ID, 'country')
        country.send_keys("Canada")

        region_id = driver.find_element(By.ID, 'region_id')
        region_id.send_keys("Ontario")

        zip = driver.find_element(By.ID, 'zip')
        zip.send_keys("N2C0C3")

        button = driver.find_element(By.XPATH,"//button[@title='Save Address']")
        button.click()

        print("Successful Test Save Address!")        
        
        time.sleep(3)
 
    def tearDown(self):
        self.driver.quit()
    
unittest.main()
