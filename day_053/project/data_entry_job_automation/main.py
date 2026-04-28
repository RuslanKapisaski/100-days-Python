import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

#--------/Step 1: Webscrape Zillow With BeautifulSoup/--------
URL = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(url=URL)
soup = BeautifulSoup(response.content, 'lxml')

lisings = soup.find_all('li', class_='ListItem-c11n-8-84-3-StyledListCardWrapper')

links = []
prices = []
addresses = []

for listing in lisings:
    try:
        link = listing.find('a', attrs={'class': 'property-card-link'})['href']
        links.append(link)
        price = listing.find('span', attrs={'class': 'PropertyCardWrapper__StyledPriceLine'}).text
        prices.append(price.split('/')[0])
        address = listing.find('address', attrs={'data-test': 'property-card-addr'}).text
        addresses.append(address.strip())
    except (AttributeError, TypeError):
        continue

#--------/Step 2: Webscrape Google Forms With Selenium And Populate The Data/--------
FORMS_URL = "https://docs.google.com/forms/d/e/1FAIpQLScMBPERsnUOZLuuR3S1hk9Nkre7sLNuIXI4EZyV2yZIUhMRYA/viewform?usp=sharing&ouid=108405146720491708383"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
user_data_dir = os.path.join(os.getcwd(), "chrome_options")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver.set_page_load_timeout(15)
wait = WebDriverWait(driver, 20)

print(f"Found {len(addresses)} listings")

for i in range(len(addresses)):
    print(f"Processing listing {i+1}/{len(addresses)}")
    driver.get(FORMS_URL)
    time.sleep(2)

    all_inputs = wait.until(ec.presence_of_all_elements_located(
        (By.XPATH, '//input[@jsname="YPqjbf"]')
    ))
    inputs = [inp for inp in all_inputs if inp.is_displayed()]

    inputs[0].click()
    inputs[0].send_keys(addresses[i])

    inputs[1].click()
    inputs[1].send_keys(prices[i])

    inputs[2].click()
    inputs[2].send_keys(links[i])

    submit = wait.until(ec.element_to_be_clickable(
        (By.XPATH, '//div[@aria-label="Submit"]')
    ))
    submit.click()
    print(f"Submitted listing {i+1}/{len(addresses)}")

input("Press any key to end the program...")
driver.quit()