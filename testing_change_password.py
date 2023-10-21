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
 
    def tearDown(self):
        self.driver.quit()
    
unittest.main()
