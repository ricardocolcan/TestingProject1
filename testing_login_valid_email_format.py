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
 
    def tearDown(self):
        self.driver.quit()
    
unittest.main()
