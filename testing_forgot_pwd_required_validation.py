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

    # Test for login user - password required 
    def test_login_user_email_success(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")

        link_sign_in = driver.find_element(By.PARTIAL_LINK_TEXT,"Sign In")
        link_sign_in.click()

        link_forgot = driver.find_element(By.PARTIAL_LINK_TEXT,"Forgot Your Password?")
        link_forgot.click()

        email_address = driver.find_element(By.ID,'email_address')
        email_address.send_keys("tmp2@gmail.com")

        button_reset = driver.find_element(By.XPATH,"//button[@class='action submit primary']//span[contains(text(), 'Reset My Password')]")
        button_reset.click()

        # If there is an account associated with tmp2@gmail.com you will receive an email with a link to reset your password.

        driver.implicitly_wait(8)

        reset_message = driver.find_element(By.XPATH,"//div[contains(text(), 'If there is an account associated with')]")
        # element = driver.find_element(By.XPATH,"//div[contains(text(), 'You saved the account information.')]")

        extracted_error = reset_message.text[:38]
        
        self.assertEqual("If there is an account associated with", extracted_error)
        
        print("Successful Test Login User with Password Validation!")       
        
        time.sleep(3)
 
    def tearDown(self):
        self.driver.quit()
    
unittest.main()
