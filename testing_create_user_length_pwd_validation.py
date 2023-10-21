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
 
    def tearDown(self):
        self.driver.quit()
    
unittest.main()
