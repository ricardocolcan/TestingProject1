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
