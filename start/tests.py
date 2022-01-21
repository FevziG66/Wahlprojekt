from lib2to3.pgen2 import driver
import time
from django.test import LiveServerTestCase, TestCase

# Create your tests here.

#Selenium Tests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class LoginTest(LiveServerTestCase):

    def testlogin(self):
        driver = webdriver.Chrome()

        #Login Seite wird aufgreufen
        driver.get('http://127.0.0.1:8000/login/')

        time.sleep(2)

        #Die Felder username und password werden durch findElementByName gefunden
        user_name = driver.find_element_by_name('username')
        user_password = driver.find_element_by_name('password')

        time.sleep(2)

        #Submit Button wird gefunden
        submit = driver.find_element_by_name('login')

        #Folgende Daten werden für Username und Passwort verwendet
        user_name.send_keys('Test')
        user_password.send_keys('Test123456')

        submit.send_keys(Keys.RETURN)

        time.sleep(2)

        #Test erfolgreich, wenn das Wort "Dashboard" nach der Anmeldung zu sehen ist.
        assert 'Dashboard' in driver.page_source

#Funktionsweise wie im Beispiel oben
class RegisterTest(LiveServerTestCase):
  def testform(self):
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:8000/register/')

    time.sleep(2)

    vorname = driver.find_element_by_name('vorname')
    nachname = driver.find_element_by_name('nachname')
    username = driver.find_element_by_name('username')
    email = driver.find_element_by_name('email')
    passwort = driver.find_element_by_name('passwort')
    passwort_wiederholen = driver.find_element_by_name('passwort_wiederholen')

    time.sleep(2)

    submit = driver.find_element_by_id('register')

    vorname.send_keys('test')
    nachname.send_keys('test')
    username.send_keys('test1')
    email.send_keys('test1@test.de')
    passwort.send_keys('123456')
    passwort_wiederholen.send_keys('123456')

    submit.send_keys(Keys.RETURN)

    time.sleep(5)

    assert 'Login' in driver.page_source