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
 
    def tearDown(self):
        self.driver.quit()
    
unittest.main()
