import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

load_dotenv()

URL = "https://tinder.com"

#---------------- / Setup Chrome Options / ----------------

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Local profile
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument("--profile-directory=Default")

# Anti-detection
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

#---------------- / Setup Driver / ----------------

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

wait = WebDriverWait(driver, 15)

#---------------- / Popup Handling / ----------------

def dismiss_popup(xpath):
    try:
        btn = wait.until(ec.element_to_be_clickable((By.XPATH, xpath)))
        btn.click()
        time.sleep(1)
    except:
        pass

def hide_blocking_overlay():
    """Hide the sticky bottom overlay that blocks button clicks"""
    try:
        driver.execute_script("""
            var divs = document.querySelectorAll('div');
            for (var d of divs) {
                var cls = d.className || '';
                if (cls.includes('Pos(f)') && cls.includes('B(0)') && cls.includes('Py(20px)')) {
                    d.style.display = 'none';
                }
            }
        """)
    except:
        pass

#---------------- / Automated Login / ----------------

PHONE_NUMBER = os.getenv("PHONE_NUMBER")

def login():
    try:
        time.sleep(2)
        login_btn = wait.until(ec.element_to_be_clickable(
            (By.XPATH, '//div[contains(text(), "Log in")]')
        ))
        print(login_btn.text)
        login_btn.click()
        time.sleep(2)

        login_with_phone_number_btn = wait.until(ec.element_to_be_clickable(
            (By.XPATH, '//button[.//div[contains(text(), "Log in with phone number")]]')
        ))
        login_with_phone_number_btn.click()

        phone_number_input = wait.until(ec.element_to_be_clickable(
            (By.ID, 'phone_number')
        ))
        phone_number_input.send_keys(PHONE_NUMBER)

        # Pause for manual puzzle solve + OTP entry
        input("🧩 Complete login in the browser, then press Enter to continue...")

    except Exception as e:
        print(f"Login error: {e}")

login()

#---------------- / Wait for Tinder to Load / ----------------

print("⏳ Waiting for Tinder to load...")
try:
    wait.until(ec.presence_of_element_located(
        (By.XPATH, '//div[contains(@class, "gamepad-button-wrapper")]')
    ))
    print("✅ Tinder loaded!")
except:
    print("⚠️ Tinder may not be fully loaded, continuing anyway...")
    time.sleep(5)

#---------------- / Like & Dislike / ----------------
likes = 0
dislikes = 0

def like(people):
    global likes
    hide_blocking_overlay()
    for i in range(people):
        time.sleep(1)
        try:
            like_btn = wait.until(ec.presence_of_element_located(
                (By.XPATH, '(//div[contains(@class, "gamepad-button-wrapper")])[4]//button')
            ))
            driver.execute_script("arguments[0].click();", like_btn)
            print("Successfully liked 1 person!")
            likes += 1

        except ElementClickInterceptedException:
            try:
                match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
                match_popup.click()
            except NoSuchElementException:
                time.sleep(2)

        except Exception as e:
            print(f"Could not find Like button: {e}")
            break

def dislike(people):
    global dislikes
    hide_blocking_overlay()
    for i in range(people):
        time.sleep(1)
        try:
            dislike_btn = wait.until(ec.presence_of_element_located(
                (By.XPATH, '(//div[contains(@class, "gamepad-button-wrapper")])[2]//button')
            ))
            driver.execute_script("arguments[0].click();", dislike_btn)
            print("Successfully disliked 1 person!")
            dislikes += 1
        except ElementClickInterceptedException:
            try:
                match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
                match_popup.click()
            except NoSuchElementException:
                time.sleep(2)

        except Exception as e:
            print(f"Could not find Dislike button: {e}")
            break

#---------------- / Report / ----------------

def print_report():
    print(f"New likes: {likes}\nNew dislikes: {dislikes}")

#---------------- / Running / ----------------

def run():
    is_running = True
    user_choice = input("Please enter your choice (like, dislike): ").lower()

    if user_choice not in ["like", "dislike"]:
        print("Invalid command, please try again.")
        return False

    people_count = int(input(f"How many people do you want to {user_choice}? "))

    if user_choice == "like":
        print("Liking mode activated...")
        like(people_count)
    elif user_choice == "dislike":
        print("Disliking mode activated...")
        dislike(people_count)

    return is_running


result = run()
print_report()
while result:
    choice = input("Do you want to continue? y/n: ")
    if choice.lower() == "n":
        break
    run()

#---------------- / Quit Selenium / ----------------

input("Press any key to exit.")
driver.quit()