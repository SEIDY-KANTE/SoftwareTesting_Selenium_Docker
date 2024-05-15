import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from django.contrib.auth.models import User


class LinkFilterTests(unittest.TestCase):

    def setUp(self):

        if not User.objects.filter(username="Seidy").exists():
            User.objects.create_superuser("Seidy", "seidy@gmail.com", "1234")

        self.URL = "http://127.0.0.1:8000/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_navlink(self):
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

        sleep(1)

        nav_list = driver.find_element(
            By.XPATH, "//*[@id='mainNavigation']/ul/li[2]/ul"
        ).find_elements(By.TAG_NAME, "li")

        nav_list_href = [
            nav.find_element(By.TAG_NAME, "a").get_attribute("href") for nav in nav_list
        ]

        driver.get(nav_list_href[0])

        sleep(1)

        is_same_page = False
        for nav in nav_list_href[1:]:

            prev_title = (
                driver.find_element(By.CLASS_NAME, "pagetitle__heading")
                .text.strip()
                .lower()
            )

            driver.find_element(
                By.XPATH, "//*[@id='mainNavigation']/ul/li[2]/a"
            ).click()

            driver.get(nav)

            sleep(2)

            driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

            sleep(1)

            driver.find_element(By.ID, "scrollTopBtn").click()

            sleep(1)

            next_title = (
                driver.find_element(By.CLASS_NAME, "pagetitle__heading")
                .text.strip()
                .lower()
            )

            is_same_page = prev_title == next_title

            if is_same_page:
                break

        if not is_same_page:
            print("Navlink test successful")
        else:
            print("Navlink test failed")

        self.assertFalse(is_same_page)

    def test_external_link(self):
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

        driver.find_element(By.XPATH, "/html/body/div/footer/div/div[3]/div/a").click()

        sleep(2)

        external_website_name = (
            driver.find_element(
                By.XPATH,
                "//*[@id='content']/div[1]/section/div[1]/div[1]/div[1]/div/a/h1",
            )
            .text.strip()
            .lower()
        )

        condition = "7oroof" == external_website_name or "https:" in driver.current_url

        if condition:
            print("External link test successful")
        else:
            print("External link test failed")

        self.assertTrue(condition)

    def test_process(self):
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

        driver.find_element(
            By.CSS_SELECTOR, "#mainNavigation > ul > li:nth-child(3) > a"
        ).click()

        sleep(1)

        driver.find_element(
            By.CSS_SELECTOR,
            "#mainNavigation > ul > li:nth-child(3) > ul > li > div > div:nth-child(1) > ul > li:nth-child(2) > a",
        ).click()

        sleep(2)

        driver.find_element(
            By.XPATH,
            "/html/body/div/section[2]/div/div/div/nav/a[3]",
        ).click()

        sleep(1)

        tabs_process = driver.find_element(
            By.XPATH, "//*[@id='work-process']/div/div/div[2]/nav"
        )

        process_list = tabs_process.find_elements(By.TAG_NAME, "a")

        process_images = []
        for process in process_list:
            process.click()
            sleep(1)

            process_images.append(
                (
                    driver.find_element(By.CLASS_NAME, "tab-content")
                    .find_element(By.CLASS_NAME, "active")
                    .find_element(By.TAG_NAME, "img")
                ).get_attribute("src"),
            )

        condition = all([image.strip() != "" for image in process_images]) and len(
            set(process_images)
        ) == len(process_images)

        if condition:
            print("Process test successful")
        else:
            print("Process test failed")

        self.assertTrue(condition)

    def test_filter(self):
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

        driver.find_element(By.XPATH, "//*[@id='mainNavigation']/ul/li[4]/a").click()

        sleep(1)

        driver.find_element(
            By.CSS_SELECTOR,
            "#mainNavigation > ul > li.nav__item.has-dropdown.show > ul > li:nth-child(2) > a",
        ).click()

        sleep(2)

        portfolio_items = driver.find_element(
            By.CLASS_NAME, "portfolio-filter"
        ).find_elements(By.TAG_NAME, "li")


        all_data = driver.find_element(By.ID, "filtered-items-wrap").find_elements(
            By.CLASS_NAME, "portfolio-item"
        )

        filtered_items = []

        for portfolio in portfolio_items[1:]:
            portfolio.click()
            sleep(1)

            data_filter = portfolio.find_element(By.TAG_NAME, "a").get_attribute(
                "data-filter"
            )

            portfolio_items = driver.find_element(By.CLASS_NAME, data_filter[1:])

            filtered_items.append(portfolio_items)


        condition = len(all_data) == len(filtered_items)

        if condition:
            print("Filter test successful")
        else:
            print("Filter test failed")

        self.assertTrue(condition)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
