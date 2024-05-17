import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User
from time import sleep


class PopupTests(unittest.TestCase):

    def setUp(self):

        # if not User.objects.filter(username="Seidy").exists():
        #     User.objects.create_superuser("Seidy", "seidy@gmail.com", "1234")

        self.URL = "http://127.0.0.1:8000/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_login_popup_active(self):

        driver = self.driver
        url = self.URL
        driver.get(url)

        sleep(3)

        login_popup_class = driver.find_element(By.ID, "login-popup").get_attribute(
            "class"
        )

        condition = "active" in login_popup_class

        if condition:
            print("Login popup active test successfull")
        else:
            print("Login popup active test successfull")

        self.assertTrue(condition)

    def test_search_popup_active(self):

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

        driver.find_element(By.CLASS_NAME, "icon-search").click()

        sleep(2)

        search_popup = driver.find_element(By.CLASS_NAME, "search-popup")

        search_popup_class = search_popup.get_attribute("class")

        condition = "active" in search_popup_class

        if condition:
            print("Search popup active test successfull")

        else:
            print("Search popup active test successfull")

        self.assertTrue(condition)

    def test_search_popup_open_close(self):
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

        driver.find_element(By.CLASS_NAME, "icon-search").click()

        sleep(2)

        search_popup = driver.find_element(By.CLASS_NAME, "search-popup")

        search_popup_active = search_popup.get_attribute("class")

        driver.find_element(By.CLASS_NAME, "search-popup__close").click()

        sleep(3)

        search_popup_inactive = search_popup.get_attribute("class")

        condition = (
            "active" in search_popup_active and "inActive" in search_popup_inactive
        )

        if condition:
            print("Search popup open and close test successfull")
        else:
            print("Search popup open and close test successfull")

        self.assertTrue(condition)


    def test_video_popup(self):
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

        driver.find_element(By.XPATH, "/html/body/div/header/nav/div/div[1]/ul/li[2]/ul/li[1]/a").click()

        sleep(2)

        driver.find_element(By.CLASS_NAME, "popup-video").click()

        sleep(2)

        condition = driver.find_element(By.CLASS_NAME, "mfp-ready").is_displayed()

        if condition:
            print("Video popup test successfull")
        else:
            print("Video popup test successfull")

        self.assertTrue(condition)

    
    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()