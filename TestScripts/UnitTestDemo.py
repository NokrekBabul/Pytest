import unittest
from selenium import webdriver

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="C:/Users/theda/PycharmProjects/TestProject/drivers/geckodriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_FacebookLogin(self):

        //Configuration


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


# if __name__ == '__main__':
#     unittest.main()
