from selenium.webdriver.common.by import By
from time import sleep


def login(driver, url):

    # sleep(15)

    driver.get(url)

    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")

    submit_button = driver.find_element(
        By.CSS_SELECTOR, "#login-popup > div > form > button > span"
    )

    username_field.send_keys("Seidy")
    password_field.send_keys("1234")
    submit_button.click()

    sleep(2)
