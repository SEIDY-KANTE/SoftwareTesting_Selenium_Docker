import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from django.contrib.auth.models import User
from SoftwareTesting_Selenium_Docker.models.industry_model import IndustryModel
from django.core import management
from SoftwareTesting_Selenium_Docker.utils import login


class TestIndustry(unittest.TestCase):

    def setUp(self):

        # if not User.objects.filter(username="Seidy").exists():
        #     User.objects.create_superuser("Seidy", "seidy@gmail.com", "1234")

        self.URL = "http://127.0.0.1:8000"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        self.driver.implicitly_wait(10)

    
    def test_add_industry_with_valid_credentials(self):

        login(self.driver, self.URL)

        self.driver.get(self.URL + "/add-industry.html")

        sleep(1)

        image_field = self.driver.find_element(By.ID, "image")
        title_field = self.driver.find_element(By.ID, "title")
        description_field = self.driver.find_element(By.ID, "description-content")
        list_item_field = self.driver.find_element(By.ID, "list-items")

        history_timeline_subtitle_field = self.driver.find_element(
            By.ID, "history-timeline-subtitle"
        )

        history_timeline_title_field = self.driver.find_element(
            By.ID, "history-timeline-title"
        )

        history_timeline_year_field = self.driver.find_element(
            By.ID, "history-timeline-year"
        )

        history_timeline_description_field = self.driver.find_element(
            By.ID, "history-timeline-description"
        )

        form_submit_button = self.driver.find_element(
            By.XPATH,
            "/html/body/div/section[2]/div/div/div/div/section/div/div/div/div/form/div/div[10]/button",
        )

        image_field.send_keys("images/services/1.jpg")
        title_field.send_keys("Software Testing")
        description_field.send_keys(
            """Software testing is a process, to evaluate the functionality of a software application with an intent to find whether the developed software met the specified requirements or not and to identify the defects to ensure that the product is defect-free in order to produce the quality product.

            Software testing involves the execution of a software component or system component to evaluate one or more properties of interest. In general, these properties indicate the extent to which the component or system under test:

            1. Meets the requirements that guided its design and development,
            2. Responds correctly to all kinds of inputs,
            3. Performs its functions within an acceptable time,
            4. Is sufficiently usable,
            5. Can be installed and run in its intended environments, and
            6. Achieves the general result its stakeholders desire.
            """
        )

        list_item_field.send_keys("Quality Assurance\n")
        list_item_field.send_keys("Software Testing\n")
        list_item_field.send_keys("Software Development\n")
        list_item_field.send_keys("Software Maintenance")

        history_timeline_subtitle_field.send_keys("Software Testing")
        history_timeline_title_field.send_keys("Software Testing")
        history_timeline_year_field.send_keys("2022\n")
        history_timeline_year_field.send_keys("2023")

        history_timeline_description_field.send_keys(
            """Software testing is a process, to evaluate the functionality of a software application with an intent to find whether the developed software met the specified requirements or not and to identify the defects to ensure that the product is defect-free in order to produce the quality product.

            Software testing involves the execution of a software component or system component to evaluate one or more properties of interest. In general, these properties indicate the extent to which the component or system under test:

            1. Meets the requirements that guided its design and development,
            2. Responds correctly to all kinds of inputs,
            3. Performs its functions within an acceptable time,
            4. Is sufficiently usable,
            5. Can be installed and run in its intended environments, and
            6. Achieves the general result its stakeholders desire.\n
            """
        )
        history_timeline_description_field.send_keys(
            """Software testing is a process, to evaluate the functionality of a software application with an intent to find whether the developed software met the specified requirements or not and to identify the defects to ensure that the product is defect-free in order to produce the quality product.

            Software testing involves the execution of a software component or system component to evaluate one or more properties of interest. In general, these properties indicate the extent to which the component or system under test:

            1. Meets the requirements that guided its design and development,
            2. Responds correctly to all kinds of inputs,
            3. Performs its functions within an acceptable time,
            4. Is sufficiently usable,
            5. Can be installed and run in its intended environments, and
            6. Achieves the general result its stakeholders desire.
            """
        )

        form_submit_button.click()

        sleep(2)

        # Assert success message

        success_message = (
            self.driver.find_element(By.CLASS_NAME, "error-title").text.strip().lower()
        )

        condition = success_message == "inudstry is saved successfully"

        if condition:
            print("Add Industry test successful")
        else:
            print("Add Industry test failed")

        self.assertTrue(condition)

    def test_add_industry_with_invalid_credentials(self):

        sleep(15)

        login(self.driver, self.URL)

        self.driver.get(self.URL + "/add-industry.html")

        sleep(2)

        form_submit_button = self.driver.find_element(
            By.XPATH,
            "/html/body/div/section[2]/div/div/div/div/section/div/div/div/div/form/div/div[10]/button",
        )

        form_submit_button.click()

        sleep(2)

        # Assert error message

        error_message = (
            self.driver.find_element(By.CLASS_NAME, "error-title").text.strip().lower()
        )

        condition = error_message == "oops! that page can’t be found."

        if condition:
            print("Invalid Add Industry test successful")
        else:
            print("Invalid Add Industry test failed")

        self.assertTrue(condition)

    def test_open_single_industry(self):
        login(self.driver, self.URL)

        self.driver.get(self.URL + "/industries.html")

        sleep(2)

        industry = self.driver.find_element(
            By.XPATH, "/html/body/div/section[2]/div/div[3]/div[1]/div/div[2]/a"
        )

        industry.click()

        sleep(3)

        self.driver.execute_script("window.scrollBy(0, 300);")

        sleep(2)

        # Assert industry page

        started_button_text = (
            self.driver.find_element(
                By.XPATH,
                "/html/body/div/section[1]/div/div/div/div/a[1]/span",
            )
            .text.strip()
            .lower()
        )

        condition = started_button_text == "get started"

        if condition:
            print("Open Single Industry test successful")
        else:
            print("Open Single Industry test failed")

        self.assertTrue(condition)

    def test_list_of_industries(self):

        login(self.driver, self.URL)

        # self.handle_loaddata()

        self.driver.get(self.URL + "/industries.html")

        sleep(2)

        self.driver.execute_script("window.scrollBy(0, 100);")

        industry_items = self.driver.find_elements(By.CLASS_NAME, "service-item")

        print("============LIST OF INDUSTRIES==================")
        i = 0
        for industry in industry_items:
            industry_image = (
                industry.find_element(By.CLASS_NAME, "service__img")
                .find_element(By.TAG_NAME, "img")
                .get_attribute("src")
            )
            industry_title = industry.find_element(
                By.CLASS_NAME, "service__title"
            ).text.strip()
            industry_description = industry.find_element(
                By.CLASS_NAME, "service__desc"
            ).text.strip()

            i += 1
            print(f"==================INDUSTRY-{i}==================")
            print(f"Industry Image: {industry_image}")
            print(f"Industry Title: {industry_title}")
            print(f"Industry Description: {industry_description}")
            print("=================================================")

        condition = len(industry_items) > 0

        if condition:
            print("List of industries test successful")
        else:
            print("List of industries test failed")

        self.assertTrue(condition)

    def test_zno_industry(self):

        login(self.driver, self.URL)

        self.driver.get(self.URL + "/industries.html")

        sleep(2)

        self.driver.find_element(By.CLASS_NAME, "delete-industries").find_element(
            By.TAG_NAME, "button"
        ).click()

        sleep(2)

        industry_title = self.driver.find_element(By.CLASS_NAME, "pagetitle__heading")

        self.driver.execute_script(
            "arguments[0].innerText = 'NO INDUSTRY TEST IS RUNNING...';", industry_title
        )

        industry_items = self.driver.find_elements(By.CLASS_NAME, "service-item")

        self.driver.execute_script("window.scrollBy(0, 100);")

        condition = len(industry_items) == 0

        if condition:
            print("No Industry test successful")
        else:
            print("No Industry test failed")

        self.assertTrue(condition)

    def tearDown(self):
        self.driver.quit()

        # if User.objects.filter(username="Seidy").exists():
        #     User.objects.filter(username="Seidy").delete()


if __name__ == "__main__":
    unittest.main()
