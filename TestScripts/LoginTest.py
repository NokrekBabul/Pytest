
import unittest

import HtmlTestRunner
from selenium import webdriver

class CapitalOneLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Firefox(executable_path="C:/Users/theda/PycharmProjects/TestProject/drivers/geckodriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_Login(self):
        self.driver.get("https://www.capitalone.com/")
        self.driver.find_element_by_id("no-acct-uid").send_keys("abcd@gmail.com")
        self.driver.find_element_by_name("no-acct-pw").send_keys("abcd1234")
        self.driver.find_element_by_css_selector("#no-acct-submit").click()

        x = self.driver.title
        print(x)
        self.assertEqual(x, "Capital One Credit Cards, Bank, and Loans - Personal and Business")


    def test_LoginNeg(self):
        self.driver.get("https://www.capitalone.com/")
        self.driver.find_element_by_id("no-acct-uid").send_keys("abcd@gmail.com")
        self.driver.find_element_by_name("no-acct-pw").send_keys("abcd1234")
        self.driver.find_element_by_css_selector("#no-acct-submit").click()

    def test_LoginPosiveN(self):
        self.driver.get("https://www.capitalone.com/")
        self.driver.find_element_by_id("no-acct-uid").send_keys("abcd@gmail.com")
        self.driver.find_element_by_name("no-acct-pw").send_keys("abcd1234")
        self.driver.find_element_by_css_selector("#no-acct-submit").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/theda/PycharmProjects/TestProject/reports", verbosity=2))
