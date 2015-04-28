import unittest
import redis
from selenium import webdriver
redis = redis.Redis(host='d1t0433g.austin.hp.com', port='6380')
keys = redis.keys('*')
raw_baseunit = redis.get('test:baseunit')

class BaseUnit(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.PhantomJS()

	def test(self):
		self.driver.get("http://elidev5.austin.hp.com/Elite/login/auth")
		self.driver.find_element_by_id('username').send_keys("ngeo_pur1")
		self.driver.find_element_by_id('password').send_keys("anything")
		self.driver.find_element_by_xpath('html/body/div[1]/div[3]/div/section/div/form/ul/li[5]/div[2]/div/input').click()
		self.driver.get("http://elidev5.austin.hp.com/Elite/customizeCTO/redis")
		self.driver.find_element_by_partial_link_text("18757424").click()
		self.driver.find_element_by_xpath(".//*[@id='tabs']/nav/ul/li[2]/a/i").click()
		Actual = self.driver.find_element_by_xpath(".//*[@id='subcat_baseModelSection.baseModelChoice']/div/div[1]").text

		keys = redis.keys('*')
		raw_baseunit = redis.get('test:baseUnit')
		print "Actual Base Unit=",Actual
		print "Expected Base Unit=",raw_baseunit
		self.assertEquals(raw_baseunit,Actual)
	
	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
    unittest.main()
