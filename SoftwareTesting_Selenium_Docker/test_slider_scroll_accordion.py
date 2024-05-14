import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from django.contrib.auth.models import User


class SliderScrollAccordionTests(unittest.TestCase):

    def setUp(self):

        self.URL = "http://127.0.0.1:8000"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_slider(self):
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

        driver.execute_script("window.scrollBy(0, 300);")

        sleep(2)

        stories = driver.find_element(
            By.XPATH, "/html/body/div/section[7]/div/div[2]/div/div/div/div"
        ).find_elements(By.CLASS_NAME, "portfolio-item")

        slick_actives = []

        for story in stories:

            if "slick-active" in story.get_attribute("class"):
                slick_actives.append(story)

        next_button = driver.find_element(By.XPATH, "//*[@id='slick-slide-control71']")

        next_button.click()

        sleep(2)

        stories = driver.find_element(
            By.XPATH, "/html/body/div/section[7]/div/div[2]/div/div/div/div"
        ).find_elements(By.CLASS_NAME, "portfolio-item")

        slick_actives_after_click = []

        for story in stories:
            if "slick-active" in story.get_attribute("class"):
                slick_actives_after_click.append(story)

        condition = slick_actives != slick_actives_after_click

        if condition:
            print("Slider test successful")
        else:
            print("Slider test failed")

        self.assertTrue(condition)

    def test_scroll(self):
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

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        sleep(2)

        scrool_to_btn = driver.find_element(By.ID, "scrollTopBtn")

        is_active = "actived" in scrool_to_btn.get_attribute("class")

        scrool_to_btn.click()

        sleep(2)

        is_desactive_after_click = "actived" not in scrool_to_btn.get_attribute("class")

        condition = is_active and is_desactive_after_click

        if condition:
            print("Scroll test successful")
        else:
            print("Scroll test failed")

        self.assertTrue(condition)

    def test_accordion(self):
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
            By.XPATH, "//*[@id='mainNavigation']/ul/li[2]/ul/li[6]/a"
        ).click()

        driver.execute_script("window.scrollBy(0, 300);")

        sleep(2)

        accordion = driver.find_element(By.CLASS_NAME, "accordion__header")

        accordion.click()

        sleep(2)

        condition = "true" == accordion.get_attribute("aria-expanded")

        if condition:
            print("Accordion test successful")
        else:
            print("Accordion test failed")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
