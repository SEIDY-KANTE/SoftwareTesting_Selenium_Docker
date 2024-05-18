import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from django.contrib.auth.models import User
from SoftwareTesting_Selenium_Docker.utils import login


class ValidationTests(unittest.TestCase):

    def setUp(self):

        # if not User.objects.filter(username="Seidy").exists():
        #     User.objects.create_superuser("Seidy", "seidy@gmail.com", "1234")

        self.URL = "http://127.0.0.1:8000"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_valid_email(self):

        sleep(15)

        login(self.driver, self.URL)

        sleep(2)

        features = self.driver.find_element(
            By.XPATH, "//*[@id='mainNavigation']/ul/li[6]/a"
        )
        features.click()

        sleep(2)

        coming_soon = self.driver.find_element(
            By.XPATH, "//*[@id='mainNavigation']/ul/li[6]/ul/li[1]/a"
        )
        coming_soon.click()

        sleep(2)

        email_field = self.driver.find_element(By.ID, "contact-email")

        email_field.send_keys("abc@gmail.com")

        subscribe_button = self.driver.find_element(
            By.XPATH, "//*[@id='contactForm']/button"
        )

        subscribe_button.click()

        sleep(2)

        # Assert email validation

        success_message = (
            self.driver.find_element(By.CLASS_NAME, "contact-result")
            .text.strip()
            .lower()
        )

        condition = success_message == "please wait..."

        if condition:
            print("Email validation test successful")
        else:
            print("Email validation test failed")

        self.assertTrue(condition)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
