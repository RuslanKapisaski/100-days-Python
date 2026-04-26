import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class InternetSpeedTwitterBot:

    def __init__(self):
        self.PROMISED_DOWN = 100
        self.PROMISED_UP = 10
        self.actual_down_speed = 0.0
        self.actual_up_speed = 0.0
        self.x_url = "https://x.com/home"

    def setup(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        self.chrome_options.add_argument(f"--user-data-dir={self.user_data_dir}")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

    def agree_policies(self, xpath):
        try:
            accept_btn = self.wait.until(ec.element_to_be_clickable((By.XPATH, xpath)))
            accept_btn.click()
        except TimeoutException:
            print("Policy button not found, continuing...")

    def get_internet_speed(self):
        self.setup()
        self.driver.get("https://www.speedtest.net/")
        self.agree_policies('//*[@id="onetrust-accept-btn-handler"]')

        try:
            go_button = self.wait.until(ec.element_to_be_clickable(
                (By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a')
            ))
            go_button.click()
        except TimeoutException:
            print("Go button not found!")
            return

        try:
            download_element = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, '.result-data-large.number.result-data-value.download-speed')
            ))
            WebDriverWait(self.driver, 60).until(
                lambda d: download_element.text.strip() not in ('', '—')
            )

            upload_element = self.wait.until(ec.visibility_of_element_located(
                (By.CSS_SELECTOR, '.result-data-large.number.result-data-value.upload-speed')
            ))
            WebDriverWait(self.driver, 60).until(
                lambda d: upload_element.text.strip() not in ('', '—')
            )

            self.actual_down_speed = float(download_element.text)
            self.actual_up_speed = float(upload_element.text)

            print("Download speed:", self.actual_down_speed)
            print("Upload speed:", self.actual_up_speed)

            self.compare_actual_vs_expected()
        except TimeoutException:
            print("Speed results not found!")
        finally:
            self.stop_bot()

    def compare_actual_vs_expected(self):
        if self.actual_down_speed < self.PROMISED_DOWN or  self.actual_up_speed < self.PROMISED_UP:
            print(f"Conditions not met! Expected: {self.PROMISED_DOWN} | Actual: {self.actual_down_speed}")
            self.write_x_post()
        else:
            print(f"Upload speed met!")

    def write_x_post(self):
        self.driver.get(self.x_url)

        message = (f'Hey, Internet Provider! Why my is {self.actual_down_speed}  '
                   f'down / {self.actual_up_speed} up when i pay for {self.PROMISED_DOWN}'
                   f' down / {self.PROMISED_UP} up  ')

        try:
            tweet_box = WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(
                (By.XPATH, '//div[@aria-label="Post text"]')
            ))
            tweet_box.click()
            tweet_box.send_keys(message)

            ## Post
            # post_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(
            #(By.XPATH, '//button[@data-testid="tweetButtonInline"]')))
            # post_button.click()
        except:
            print("Tweet box not found!")

    def stop_bot(self):
        input("Press Enter to exit...")
        self.driver.quit()