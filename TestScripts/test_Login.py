from selenium import webdriver
import pytest

class TestLogin():
    #codingandtestingdaily@gmail.com
    @pytest.fixture()
    def test_setUp(self):
        global driver
        driver = webdriver.Firefox(executable_path="C:\\Users\\theda\\PycharmProjects\\TestProject\\drivers\\geckodriver.exe")
        driver.implicitly_wait(5)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()

    def test_Login_1(self, test_setUp):
        driver.get("https://www.facebook.com/")
        driver.find_element_by_name("email").send_keys("abcd@gmail.com")
        driver.find_element_by_id("pass").send_keys("abcd1234")
        driver.find_element_by_css_selector("#u_0_2").click()

        x = driver.title
        print(x)
        assert x == "Facebook - Log In or Sign Up"

    def test_Login_2(self, test_setUp):
        driver.get("https://www.facebook.com/")
        driver.find_element_by_name("email").send_keys("nokrekbabul@gmail.com")
        driver.find_element_by_id("pass").send_keys("abcd1234")
        driver.find_element_by_css_selector("#u_0_2").click()

    def test_Login_3(self, test_setUp):
        driver.get("https://www.facebook.com/")
        driver.find_element_by_name("email").send_keys("nokrekbabul@gmail.com")
        driver.find_element_by_id("pass").send_keys("abcd1235")
        driver.find_element_by_css_selector("#u_0_2").click()

    def test_Login_4(self, test_setUp):
        driver.get("https://www.facebook.com/")
        driver.find_element_by_name("emal").send_keys("nokrekbabul@gmail.com")
        driver.find_element_by_id("pass").send_keys("abcd1235")
        driver.find_element_by_css_selector("#u_0_2").click()

# if __name__ == '__main__':
#     pytest.main(verbosity=2)