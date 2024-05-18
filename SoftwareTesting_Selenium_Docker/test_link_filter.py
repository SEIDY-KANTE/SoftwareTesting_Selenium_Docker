import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from django.contrib.auth.models import User
from SoftwareTesting_Selenium_Docker.utils import login


class LinkFilterTests(unittest.TestCase):

    def setUp(self):

        # if not User.objects.filter(username="Seidy").exists():
        #     User.objects.create_superuser("Seidy", "seidy@gmail.com", "1234")

        self.URL = "http://127.0.0.1:8000/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_navlink(self):
        login(self.driver, self.URL)

        self.driver.find_element(By.XPATH, "//*[@id='mainNavigation']/ul/li[2]/a").click()

        sleep(1)

        nav_list = self.driver.find_element(
            By.XPATH, "//*[@id='mainNavigation']/ul/li[2]/ul"
        ).find_elements(By.TAG_NAME, "li")

        nav_list_href = [
            nav.find_element(By.TAG_NAME, "a").get_attribute("href") for nav in nav_list
        ]

        self.driver.get(nav_list_href[0])

        sleep(1)

        is_same_page = False
        for nav in nav_list_href[1:]:

            prev_title = (
                self.driver.find_element(By.CLASS_NAME, "pagetitle__heading")
                .text.strip()
                .lower()
            )

            self.driver.find_element(
                By.XPATH, "//*[@id='mainNavigation']/ul/li[2]/a"
            ).click()

            self.driver.get(nav)

            sleep(2)

            self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

            sleep(1)

            self.driver.find_element(By.ID, "scrollTopBtn").click()

            sleep(1)

            next_title = (
                self.driver.find_element(By.CLASS_NAME, "pagetitle__heading")
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

        sleep(15)

        login(self.driver, self.URL)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        sleep(2)

        self.driver.find_element(By.XPATH, "/html/body/div/footer/div/div[3]/div/a").click()

        sleep(2)

        external_website_name = (
            self.driver.find_element(
                By.XPATH,
                "//*[@id='content']/div[1]/section/div[1]/div[1]/div[1]/div/a/h1",
            )
            .text.strip()
            .lower()
        )

        condition = "7oroof" == external_website_name or "https:" in self.driver.current_url

        if condition:
            print("External link test successful")
        else:
            print("External link test failed")

        self.assertTrue(condition)

    def test_process(self):

        login(self.driver, self.URL)

        self.driver.find_element(
            By.CSS_SELECTOR, "#mainNavigation > ul > li:nth-child(3) > a"
        ).click()

        sleep(1)

        self.driver.find_element(
            By.CSS_SELECTOR,
            "#mainNavigation > ul > li:nth-child(3) > ul > li > div > div:nth-child(1) > ul > li:nth-child(2) > a",
        ).click()

        sleep(2)

        self.driver.find_element(
            By.XPATH,
            "/html/body/div/section[2]/div/div/div/nav/a[3]",
        ).click()

        sleep(1)

        tabs_process = self.driver.find_element(
            By.XPATH, "//*[@id='work-process']/div/div/div[2]/nav"
        )

        process_list = tabs_process.find_elements(By.TAG_NAME, "a")

        process_images = []
        for process in process_list:
            process.click()
            sleep(1)

            process_images.append(
                (
                    self.driver.find_element(By.CLASS_NAME, "tab-content")
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

        login(self.driver, self.URL)

        self.driver.find_element(By.XPATH, "//*[@id='mainNavigation']/ul/li[4]/a").click()

        sleep(1)

        self.driver.find_element(
            By.CSS_SELECTOR,
            "#mainNavigation > ul > li.nav__item.has-dropdown.show > ul > li:nth-child(2) > a",
        ).click()

        sleep(2)

        portfolio_items = self.driver.find_element(
            By.CLASS_NAME, "portfolio-filter"
        ).find_elements(By.TAG_NAME, "li")


        all_data = self.driver.find_element(By.ID, "filtered-items-wrap").find_elements(
            By.CLASS_NAME, "portfolio-item"
        )

        filtered_items = []

        for portfolio in portfolio_items[1:]:
            portfolio.click()
            sleep(1)

            data_filter = portfolio.find_element(By.TAG_NAME, "a").get_attribute(
                "data-filter"
            )

            portfolio_items = self.driver.find_element(By.CLASS_NAME, data_filter[1:])

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
