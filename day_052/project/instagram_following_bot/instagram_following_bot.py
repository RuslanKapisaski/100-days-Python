import os
import random
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

load_dotenv()

class InstagramFollowingBot:
    def __init__(self):
        self.URL = "https://instagram.com"
        self.EMAIL = os.getenv("EMAIL")
        self.PASSWORD = os.getenv("PASSWORD")
        self.SIMILAR_ACCOUNT = os.getenv("SIMILAR_ACCOUNT")

    def setup(self):
        self.user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.chrome_options.add_argument(f"--user-data-dir={self.user_data_dir}")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.wait = WebDriverWait(self.driver, 5)

    def login(self):
        self.driver.get(self.URL)
        self.allow_cookies()
        try:
            email_input = self.wait.until(ec.element_to_be_clickable((By.NAME, 'username')))
            email_input.send_keys(self.EMAIL)

            password_input = self.wait.until(ec.element_to_be_clickable((By.NAME, 'password')))
            password_input.send_keys(self.PASSWORD)
            password_input.send_keys(Keys.RETURN)

            print("Logged in successfully!")
        except TimeoutException:
            print("Unable to login — you may already be logged in.")

    def allow_cookies(self):
        try:
            cookies_button = self.wait.until(ec.element_to_be_clickable(
                (By.XPATH, '//button[text()="Allow all cookies"]')
            ))
            cookies_button.click()
        except TimeoutException:
            print("No cookie popup found, continuing...")

    def follow(self):
        while True:
            try:
                N = int(input("Enter the number of followers to follow: "))
                if N > 0:
                    break
                print("Please enter a positive number.")
            except ValueError:
                print("Please enter a valid integer.")

        try:
            print("Step 1: Clicking search button...")
            search_button = self.wait.until(ec.element_to_be_clickable(
                (By.XPATH, '//a[.//*[@aria-label="Search"]]')
            ))
            search_button.click()
            time.sleep(1)

            print("Step 2: Typing in search input...")
            search_input = self.wait.until(ec.element_to_be_clickable(
                (By.XPATH, '//input[@aria-label="Search input"]')
            ))
            search_input.send_keys(self.SIMILAR_ACCOUNT)
            time.sleep(2)

            print("Step 3: Clicking first result...")
            first_result = self.wait.until(ec.element_to_be_clickable(
                (By.XPATH, f'//a[@href="/{self.SIMILAR_ACCOUNT}/"]')
            ))
            first_result.click()
            time.sleep(2)

            print("Step 4: Clicking followers link...")
            followers_anchor_tag = self.wait.until(ec.element_to_be_clickable(
                (By.XPATH, f'//a[contains(@href, "/{self.SIMILAR_ACCOUNT}/followers/")]')
            ))
            followers_anchor_tag.click()
            time.sleep(2)

            print("Step 5: Finding follow buttons...")
            follow_buttons = self.wait.until(ec.presence_of_all_elements_located(
                (By.XPATH, '//button[@type="button"][.//div[text()="Follow"]]')
            ))

            if len(follow_buttons) < N:
                print(f"Warning: only {len(follow_buttons)} buttons found, following all of them.")

            print(f"Step 6: Following {min(N, len(follow_buttons))} accounts...")
            for button in follow_buttons[:N]:
                button.click()
                time.sleep(random.uniform(2, 5))

            print("Done!")

        except TimeoutException as e:
            print(f"Following procedure failed: {e}")

    def stop(self):
        input("Press Enter to stop the bot...")
        self.driver.quit()

    def run(self):
        self.setup()
        self.login()
        self.follow()
        self.stop()