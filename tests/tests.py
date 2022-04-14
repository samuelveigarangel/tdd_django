from django.test import LiveServerTestCase
from selenium import webdriver


class AnimaisTestCase(LiveServerTestCase):

        def setUp(self):
            self.browser = webdriver.Chrome('C:\Users\samue\PycharmProjects\tdd_django3')

        def tearDown(self):
            self.browser.quit()