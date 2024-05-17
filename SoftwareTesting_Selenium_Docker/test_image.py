import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from django.contrib.auth.models import User


class ImageTests(unittest.TestCase):

    def setUp(self):

        # if not User.objects.filter(username="Seidy").exists():
        #     User.objects.create_superuser("Seidy", "seidy@gmail.com", "1234")

        self.URL = "http://127.0.0.1:8000/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_image(self):
        driver = self.driver
        url = self.URL
        driver.get(url)

        sleep(2)

        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")

        submit_button = driver.find_element(
            By.CSS_SELECTOR, "#login-popup > div > form > button > span"
        )

        username_field.send_keys("Seidy")
        password_field.send_keys("1234")
        submit_button.click()

        sleep(2)

        driver.find_element(By.XPATH, "//*[@id='mainNavigation']/ul/li[2]/a").click()

        sleep(2)

        driver.find_element(
            By.XPATH, "//*[@id='mainNavigation']/ul/li[2]/ul/li[2]/a"
        ).click()

        sleep(2)

        driver.execute_script("window.scrollBy(0, 400);")

        sleep(2)

        image_src = (
            driver.find_element(By.CLASS_NAME, "about__img")
            .find_element(By.TAG_NAME, "img")
            .get_attribute("src")
        )

        if image_src.strip() != "":
            driver.get(image_src)
            sleep(2)
            condition = driver.find_element(By.XPATH, "/html/body/img").is_displayed()

        if condition:
            print("Image test successful")
        else:
            print("Image test failed")

        self.assertTrue(condition)

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
