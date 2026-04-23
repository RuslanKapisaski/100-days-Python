from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
interactions = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')
print(interactions.text)

driver.quit()