import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from django.contrib.auth.models import User
from SoftwareTesting_Selenium_Docker.models.blog_model import BlogModel
from django.core import management
from SoftwareTesting_Selenium_Docker.utils import login


class BlogTests(unittest.TestCase):

    def setUp(self):

        # if not User.objects.filter(username="Seidy").exists():
        #     User.objects.create_superuser("Seidy", "seidy@gmail.com", "1234")

        self.URL = "http://127.0.0.1:8000"

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def test_add_blog_with_valid_credentials(self):

        login(self.driver, self.URL)

        self.driver.get(self.URL + "/add-blog.html")

        sleep(2)

        image_field = self.driver.find_element(By.NAME, "image")
        blog_title = self.driver.find_element(By.NAME, "title")
        content_field = self.driver.find_element(By.NAME, "content")
        author_field = self.driver.find_element(By.NAME, "author")

        form_submit_button = self.driver.find_element(
            By.CSS_SELECTOR,
            "body > div > section.services-layout1.services-carousel.pb-100.bg-img > div > div > div > div > section > div > div > div > div > form > div > div.col-12 > button",
        )

        image_field.send_keys("images/blog/grid/5.jpg")
        blog_title.send_keys("Django Testing with Selenium")
        content_field.send_keys(
            """Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, Django takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

            Ridiculously fast.
            Django was designed to help developers take applications from concept to completion as quickly as possible.

            Reassuringly secure.
            Django takes security seriously and helps developers avoid many common security mistakes.

            Exceedingly scalable.
            Some of the busiest sites on the Web leverage Django’s ability to quickly and flexibly scale.

            Incredibly versatile.
            Companies, organizations, and governments have used Django to build all sorts of things — from content management systems to social networks to scientific computing platforms.

            Easy to learn.
            Django was designed to help developers take applications from concept to completion as quickly as possible.

                            """
        )
        author_field.send_keys("Seidy")

        form_submit_button.click()

        sleep(2)

        success_message = (
            self.driver.find_element(By.CLASS_NAME, "error-title").text.strip().lower()
        )

        condition = success_message == "blog post is saved successfully"

        if condition:
            print("Add Blog test successful")
        else:
            print("Add Blog test failed")

        self.assertTrue(condition)

    def test_add_blog_with_invalid_credentials(self):

        sleep(15)

        login(self.driver, self.URL)

        self.driver.get(self.URL + "/add-blog.html")

        sleep(3)

        form_submit_button = self.driver.find_element(
            By.CSS_SELECTOR,
            "body > div > section.services-layout1.services-carousel.pb-100.bg-img > div > div > div > div > section > div > div > div > div > form > div > div.col-12 > button",
        )

        form_submit_button.click()

        sleep(2)

        # Assert error message
        error_message = (
            self.driver.find_element(By.CLASS_NAME, "error-title").text.strip().lower()
        )

        # print("Error message: ", error_message)

        condition = error_message == "oops! that page can’t be found."

        if condition:
            print("Invalid Add Blog test successful")
        else:
            print("Invalid Add Blog test failed")

        self.assertTrue(condition)

    def test_select_option(self):
       
        login(self.driver, self.URL)

        self.driver.get(self.URL + "/add-blog.html")

        sleep(3)

        list_options = self.driver.find_element(By.CLASS_NAME, "list").find_elements(
            By.TAG_NAME, "li"
        )

        current_option = self.driver.find_element(By.CLASS_NAME, "current")

        for option in list_options:
            if option.get_attribute("data-value") == "Business":

                self.driver.execute_script(
                    "arguments[0].innerText = 'Business'", current_option
                )

                sleep(2)

                break

        selected_option = self.driver.find_element(
            By.XPATH,
            "/html/body/div/section[2]/div/div/div/div/section/div/div/div/div/form/div/div[4]/div/div/span",
        )

        condition = selected_option.text == "Business"

        if condition:
            print("Select Option test successful")
        else:
            print("Select Option test failed")

        self.assertTrue(condition)

    def test_open_single_blog(self):
       
        login(self.driver, self.URL)

        self.driver.get(self.URL + "/blog.html")

        sleep(3)

        blog_post = self.driver.find_element(
            By.XPATH, "/html/body/div/section[2]/div/div[2]/div[1]/div/div[2]/a"
        )

        blog_post.click()

        sleep(3)

        self.driver.execute_script("window.scrollBy(0, 200);")

        sleep(2)

        is_sidebar_visible = self.driver.find_element(
            By.CLASS_NAME, "sidebar"
        ).is_displayed()

        if is_sidebar_visible:
            print("Open Single Blog test successful")
        else:
            print("Open Single Blog test failed")

        self.assertTrue(is_sidebar_visible)

    def test_list_of_blogs(self):
       
        login(self.driver, self.URL)

        # self.handle_loaddata()

        self.driver.get(self.URL + "/blog.html")

        sleep(2)

        self.driver.execute_script("window.scrollBy(0, 100);")

        blog_posts = self.driver.find_elements(By.CLASS_NAME, "post-item")

        print("==========LIST OF BLOG POST================")
        i = 0
        for post in blog_posts:
            post_image = (
                post.find_element(By.CLASS_NAME, "post__img")
                .find_element(By.TAG_NAME, "img")
                .get_attribute("src")
            )
            post_title = (
                post.find_element(By.CLASS_NAME, "post__title")
                .find_element(By.TAG_NAME, "a")
                .text.strip()
            )
            post_category = post.find_element(
                By.CLASS_NAME, "post__meta-cat"
            ).text.strip()
            post_date = post.find_element(By.CLASS_NAME, "post__meta-date").text.strip()
            post_description = post.find_element(
                By.CLASS_NAME, "post__desc"
            ).text.strip()

            i += 1
            print(f"=================Post-{i}===================")
            print(f"Post Image: {post_image}")
            print(f"Post Title: {post_title}")
            print(f"Post Category: {post_category}")
            print(f"Post Date: {post_date}")
            print(f"Post Description: {post_description}")
            print("============================================")

        condition = len(blog_posts) > 0

        if condition:
            print("List of Blogs test successful")
        else:
            print("List of Blogs test failed")

        self.assertTrue(condition)

    def test_zno_blog_post(self):

        login(self.driver, self.URL)

        self.driver.get(self.URL + "/blog.html")

        sleep(2)

        self.driver.find_element(By.CLASS_NAME, "delete-blogs").find_element(
            By.TAG_NAME, "button"
        ).click()

        sleep(2)

        blog_title = self.driver.find_element(By.CLASS_NAME, "pagetitle__heading")

        self.driver.execute_script(
            "arguments[0].innerText = 'NO BLOG POST TEST IS RUNNING...';", blog_title
        )

        blog_posts = self.driver.find_elements(By.CLASS_NAME, "post-item")

        condition = len(blog_posts) == 0

        if condition:
            print("No Blog Post test successful")
        else:
            print("No Blog Post test failed")

        self.assertTrue(condition)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
