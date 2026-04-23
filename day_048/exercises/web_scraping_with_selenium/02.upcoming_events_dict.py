from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")

upcoming_events_menu = driver.find_element(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
events = upcoming_events_menu.find_elements(By.TAG_NAME,'li')

upcoming_events_dict = {}
event_dict = {}

for i in range(len(events)):
    event_time = events[i].find_element(By.TAG_NAME,'time').text
    event_link = events[i].find_element(By.TAG_NAME,'a').text

    event_dict[i] = {
        event_time: event_link,
    }

    upcoming_events_dict[i] = event_dict

print(upcoming_events_dict)

driver.quit()