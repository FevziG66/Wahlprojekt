from lib2to3.pgen2 import driver
import time
from django.test import LiveServerTestCase, TestCase

# Create your tests here.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class receiptTest(LiveServerTestCase):

    def testReceipt(self):
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

        driver.get('http://127.0.0.1:8000/editReceipts/')

        time.sleep(2)

        belegnummer = driver.find_element_by_name('belegnummer')
        belegdatum = driver.find_element_by_name('belegdatum')
        zahlart = driver.find_element_by_name('zahlart')
        faelligkeit = driver.find_element_by_name('faelligkeit')
        betrag = driver.find_element_by_name('betrag')
        beschreibung = driver.find_element_by_name('beschreibung')
        konto_name = driver.find_element_by_name('konto_name')
        art = driver.find_element_by_name('art')

        time.sleep(2)

        submit = driver.find_element_by_name('submit')

        belegnummer.send_keys('1')
        belegdatum.send_keys('13.01.2022')
        zahlart.send_keys('Karte')
        faelligkeit.send_keys('15.01.2022')
        betrag.send_keys('1')
        beschreibung.send_keys('Test')
        konto_name.send_keys('Büromaterial')
        art.send_keys('Einnahme')
        

        submit.send_keys(Keys.RETURN)

        time.sleep(1)

        assert 'Belege Hochladen' in driver.page_source

class contactTest(LiveServerTestCase):

    def testContact(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/login/')

        time.sleep(1)

        user_name = driver.find_element_by_name('username')
        user_password = driver.find_element_by_name('password')

        time.sleep(1)

        submit = driver.find_element_by_name('login')

        user_name.send_keys('Test')
        user_password.send_keys('Test1234')

        submit.send_keys(Keys.RETURN)

        time.sleep(1)

        assert 'Dashboard' in driver.page_source

        driver.get('http://127.0.0.1:8000/contacts/')
        driver.get('http://127.0.0.1:8000/editContacts/')

        time.sleep(2)

        firma = driver.find_element_by_name('firma')
        kontaktnummer = driver.find_element_by_name('kontaktnummer')
        ansprechpartner = driver.find_element_by_name('ansprechpartner')
        email = driver.find_element_by_name('email')
        adresse = driver.find_element_by_name('adresse')
        telefonnummer = driver.find_element_by_name('telefonnummer')

        time.sleep(2)

        submit = driver.find_element_by_name('submit')

        firma.send_keys('Musterfirma')
        kontaktnummer.send_keys('2')
        ansprechpartner.send_keys('Max Mustermann')
        email.send_keys('test@gmail.com')
        adresse.send_keys('Musterstadt')
        telefonnummer.send_keys('123456789')
        

        submit.send_keys(Keys.RETURN)

        time.sleep(1)

        assert 'erfolgreich' in driver.page_source
