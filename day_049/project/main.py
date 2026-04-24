import os
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

ACCOUNT_EMAIL = "student@test.com"
ACCOUNT_PASSWORD = "password123"
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

wait = WebDriverWait(driver, 10)

BOOKED_CLASSES = 0
WAITLIST_JOINED = 0
ALREADY_BOOKED = 0

# ----------------  Retry Wrapper ----------------

def retry(func, retries=10, description=None):
    """Takes any function and retries it up to `retries` times."""
    for attempt in range(1, retries + 1):
        print(f"Attempt {attempt}: {description or func.__name__}")
        result = func()
        if result:
            print(f"Success: {description or func.__name__}")
            return result
        print(f"Failed, retrying...")
        time.sleep(1)
    print(f"Gave up after {retries} attempts: {description or func.__name__}")
    return False

# ----------------  Login Function ----------------

def login():
    try:
        driver.get(GYM_URL)
        # Click login button
        login_btn = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
        login_btn.click()

        # Fill email
        email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
        email_input.clear()
        email_input.send_keys(ACCOUNT_EMAIL)

        # Fill password
        password_input = driver.find_element(By.ID, "password-input")
        password_input.clear()
        password_input.send_keys(ACCOUNT_PASSWORD)

        # Submit
        driver.find_element(By.ID, "submit-button").click()

        # Check success — schedule page must appear
        wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))
        return True
    except (TimeoutException, WebDriverException):
        return False

# ----------------  Book Class Function ----------------

def book_class(card, day_title, time_text):
    global BOOKED_CLASSES, WAITLIST_JOINED, ALREADY_BOOKED

    if "6:00 PM" not in time_text:
        return True

    class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
    button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

    def attempt_booking():
        try:
            btn = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            btn_text = btn.text.strip()

            if btn_text == "Booked":
                return "already_booked"
            elif btn_text == "Waitlisted":
                return "already_booked"
            elif btn_text == "Book Class":
                btn.click()
                wait.until(lambda d: card.find_element(
                    By.CSS_SELECTOR, "button[id^='book-button-']").text == "Booked"
                )
                print(f"✓ Successfully booked: {class_name} on {day_title}")
                return "booked"
            elif btn_text == "Join Waitlist":
                btn.click()
                # Confirm button changed to "Waitlisted"
                wait.until(lambda d: card.find_element(
                    By.CSS_SELECTOR, "button[id^='book-button-']").text == "Waitlisted"
                )
                print(f"✓ Joined waitlist for: {class_name} on {day_title}")
                return "waitlisted"
        except (TimeoutException, WebDriverException):
            return False

    result = retry(attempt_booking, retries=7, description=f"Book {class_name}")

    if result == "booked":
        BOOKED_CLASSES += 1
    elif result == "waitlisted":
        WAITLIST_JOINED += 1
    elif result == "already_booked":
        ALREADY_BOOKED += 1

# ----------------  Run ----------------

retry(login, retries=7, description="Login")

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text
    time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text

    if "Tue" in day_title or "Thu" in day_title:
        book_class(card, day_title, time_text)

TOTAL = BOOKED_CLASSES + WAITLIST_JOINED + ALREADY_BOOKED

print(f"\n--- BOOKING SUMMARY ---"
      f"\nNew bookings:              {BOOKED_CLASSES}"
      f"\nNew waitlist entries:      {WAITLIST_JOINED}"
      f"\nAlready booked/waitlisted: {ALREADY_BOOKED}"
      f"\nTotal Tue & Thu 6pm processed: {TOTAL}")

input("\nPress Enter to quit...")
driver.quit()