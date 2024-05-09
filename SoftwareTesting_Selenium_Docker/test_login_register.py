import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


class LoginRegisterTests(unittest.TestCase):
    def setUp(self):

        self.URL = "http://127.0.0.1:8000"

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_login_with_valid_credentials(self):
        driver = self.driver
        url = self.URL
        driver.get(url)

        # Valid credentials
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
       
        submit_button = driver.find_element(
            By.CSS_SELECTOR, "#login-popup > div > form > button > span"
        )

        username_field.send_keys("Seidy")
        password_field.send_keys("1234")
        submit_button.click()

        sleep(1)

        # Assert login success
        index_page_title = (
            driver.find_element(By.CLASS_NAME, "slide__title").text.strip().lower()
        )

        condition = index_page_title == "help challenge critical activities"

        if condition:
            print("Login test successful")

        else:
            print("Login test failed")

        self.assertTrue(condition)

    def test_login_with_invalid_credentials(self):
        driver = self.driver
        url = self.URL
        driver.get(url)

        # Invalid credentials
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")

        submit_button = driver.find_element(
            By.CSS_SELECTOR, "#login-popup > div > form > button > span"
        )

        username_field.send_keys("WrongUser")
        password_field.send_keys("WrongPassword")
        submit_button.click()

        # Assert error message
        error_message = (
            driver.find_element(By.CLASS_NAME, "error-message").text.strip().lower()
        )

        condition = error_message == "invalid username or password!"

        if condition:
            print("Login Failed test successful")
        else:
            print("Login Failed test failed")

        self.assertTrue(condition)


    def test_register_with_valid_data(self):
        driver = self.driver
        url = self.URL + "/register.html"
        driver.get(url)

        # Valid registration data

        username_field = driver.find_element(By.NAME, "username")
        email_fiel = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")

        submit_button = driver.find_element(
            By.CSS_SELECTOR, "#register-popup > div > form > button > span"
        )

        username_field.send_keys("TestUser")
        email_fiel.send_keys("test@gmail.com")
        password_field.send_keys("TestPassword")
        submit_button.click()

        sleep(2)
        # Assert registration success
        success_message = (
            driver.find_element(By.CLASS_NAME, "error-title").text.strip().lower()
        )

        condition = success_message == "user is registered successfully"

        if condition:
            print("Registration test successful")
        else:
            print("Registration test failed")

        self.assertTrue(condition)

    def test_register_with_invalid_data(self):
        driver = self.driver
        url = self.URL + "/register.html"
        driver.get(url)

        # Invalid registration data

        username_field = driver.find_element(By.NAME, "username")
        email_fiel = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")

        submit_button = driver.find_element(
            By.CSS_SELECTOR, "#register-popup > div > form > button > span"
        )

        username_field.send_keys("")
        email_fiel.send_keys("")
        password_field.send_keys("")
        submit_button.click()

        # Assert error message
        error_message = (
            driver.find_element(By.CLASS_NAME, "error-message").text.strip().lower()
        )

        condition = error_message == "all fields are required"

        if condition:
            print("Registration Failed test successful")
        else:
            print("Registration Failed test failed")

        self.assertTrue(condition)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
