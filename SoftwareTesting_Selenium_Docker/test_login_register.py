import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from django.contrib.auth.models import User
from SoftwareTesting_Selenium_Docker.utils import login


class LoginRegisterTests(unittest.TestCase):
    def setUp(self):

        # if not User.objects.filter(username="Seidy").exists():
        #     User.objects.create_superuser("Seidy", "seidy@gmail.com", "1234")

        self.URL = "http://127.0.0.1:8000"

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_login_with_valid_credentials(self):

        login(self.driver, self.URL)

        # Assert login success
        index_page_title = (
            self.driver.find_element(By.CLASS_NAME, "slide__title").text.strip().lower()
        )

        condition = index_page_title == "help challenge critical activities"

        if condition:
            print("Login test successful")

        else:
            print("Login test failed")

        self.assertTrue(condition)

    def test_login_with_invalid_credentials(self):
      
        self.driver.get(self.URL)

        # Invalid credentials
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")

        submit_button = self.driver.find_element(
            By.CSS_SELECTOR, "#login-popup > div > form > button > span"
        )

        username_field.send_keys("WrongUser")
        password_field.send_keys("WrongPassword")
        submit_button.click()

        sleep(2)

        # Assert error message
        error_message = (
            self.driver.find_element(By.CLASS_NAME, "error-message").text.strip().lower()
        )

        condition = error_message == "invalid username or password!"

        if condition:
            print("Login Failed test successful")
        else:
            print("Login Failed test failed")

        self.assertTrue(condition)

    def test_login_with_empty_fields(self):

        sleep(15)
      
        self.driver.get(self.URL)

        # Empty fields
        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")

        submit_button = self.driver.find_element(
            By.CSS_SELECTOR, "#login-popup > div > form > button > span"
        )

        username_field.send_keys(" ")
        password_field.send_keys(" ")
        submit_button.click()

        sleep(2)

        # Assert error message
        error_message = (
            self.driver.find_element(By.CLASS_NAME, "error-message").text.strip().lower()
        )

        condition = error_message == "all fields are required"

        if condition:
            print("Empty Fields test successful")
        else:
            print("Empty Fields test failed")

        self.assertTrue(condition)

    def test_register_with_valid_data(self):
        
        url = self.URL + "/register.html"
        self.driver.get(url)

        # Valid registration data

        username_field = self.driver.find_element(By.NAME, "username")
        email_fiel = self.driver.find_element(By.NAME, "email")
        password_field = self.driver.find_element(By.NAME, "password")

        submit_button = self.driver.find_element(
            By.CSS_SELECTOR, "#register-popup > div > form > button > span"
        )

        username_field.send_keys("TestUser")
        email_fiel.send_keys("test@gmail.com")
        password_field.send_keys("TestPassword")
        submit_button.click()

        sleep(2)
        # Assert registration success
        success_message = (
            self.driver.find_element(By.CLASS_NAME, "error-title").text.strip().lower()
        )

        condition = success_message == "user is registered successfully"

        if condition:
            print("Registration test successful")
        else:
            print("Registration test failed")

        self.assertTrue(condition)

    def test_register_with_invalid_data(self):
    
        url = self.URL + "/register.html"
        self.driver.get(url)

        # Invalid registration data

        username_field = self.driver.find_element(By.NAME, "username")
        email_fiel = self.driver.find_element(By.NAME, "email")
        password_field = self.driver.find_element(By.NAME, "password")

        submit_button = self.driver.find_element(
            By.CSS_SELECTOR, "#register-popup > div > form > button > span"
        )

        username_field.send_keys("")
        email_fiel.send_keys("")
        password_field.send_keys("")
        submit_button.click()

        sleep(2)

        # Assert error message
        error_message = (
            self.driver.find_element(By.CLASS_NAME, "error-message").text.strip().lower()
        )

        condition = error_message == "all fields are required"

        if condition:
            print("Registration Failed test successful")
        else:
            print("Registration Failed test failed")

        self.assertTrue(condition)

    def test_register_with_existing_username(self):
        
        url = self.URL + "/register.html"
        self.driver.get(url)

        # Registration with existing username
        username_field = self.driver.find_element(By.NAME, "username")
        email_fiel = self.driver.find_element(By.NAME, "email")
        password_field = self.driver.find_element(By.NAME, "password")

        submit_button = self.driver.find_element(
            By.CSS_SELECTOR, "#register-popup > div > form > button > span"
        )

        username_field.send_keys("Seidy")
        email_fiel.send_keys("seidy@gmail.com")
        password_field.send_keys("1234")
        submit_button.click()

        sleep(2)

        # Assert error message
        error_message = (
            self.driver.find_element(By.CLASS_NAME, "error-message").text.strip().lower()
        )

        condition = error_message == "username or email already exists!"

        if condition:
            print("Existing Username test successful")
        else:
            print("Existing Username test failed")

        self.assertTrue(condition)

    def test_logout(self):
    
        self.driver.get(self.URL)

        username_field = self.driver.find_element(By.NAME, "username")
        password_field = self.driver.find_element(By.NAME, "password")

        submit_button = self.driver.find_element(
            By.CSS_SELECTOR, "#login-popup > div > form > button > span"
        )

        username_field.send_keys("Seidy")
        password_field.send_keys("1234")
        submit_button.click()

        sleep(3)

        logout_button = self.driver.find_element(
            By.XPATH, "/html/body/div/header/nav/div/div[1]/ul/li[2]/ul/li[2]/button"
        )

        logout_button.click()

        sleep(2)

        user_profile = (
            self.driver.find_element(
                By.XPATH, "/html/body/div/header/nav/div/div/ul/li/ul/li/button/span"
            )
            .text.strip()
            .lower()
        )

        condition = user_profile == "login"

        if condition:
            print("Logout test successful")
        else:
            print("Logout test failed")

        self.assertTrue(condition)

    def tearDown(self):
        self.driver.quit()
    
        #if User.objects.filter(username="Seidy").exists():
            # User.objects.get(username="Seidy").delete()
            # print("Seidy user deleted")

        # if User.objects.filter(username="TestUser").exists():
        # User.objects.get(username="TestUser").delete()
        # print("TestUser deleted")


if __name__ == "__main__":
    unittest.main()
