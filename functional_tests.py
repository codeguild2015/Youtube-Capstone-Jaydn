from selenium import 
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		browser.quit()

	def pageStart(self):
		self.browser.get('http://localhost:8000')


if __name__ == '__main__':
	unittest.main(warnings='ignore')
