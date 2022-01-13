from lib2to3.pgen2 import driver
import time
from django.test import LiveServerTestCase, TestCase

# Create your tests here.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class LoginTest(LiveServerTestCase):

    def testlogin(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/login/')

        time.sleep(2)

        user_name = driver.find_element_by_name('username')
        user_password = driver.find_element_by_name('password')

        time.sleep(2)

        submit = driver.find_element_by_name('login')

        user_name.send_keys('Test')
        user_password.send_keys('Test1234')

        submit.send_keys(Keys.RETURN)

        time.sleep(2)

        assert 'Dashboard' in driver.page_source