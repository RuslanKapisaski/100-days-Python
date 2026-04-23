from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://cookieclicker-unblocked-online.github.io/")

coookie = driver.find_element(By.ID, "bigCookie")

while True:
    coookie.click()

driver.quit()