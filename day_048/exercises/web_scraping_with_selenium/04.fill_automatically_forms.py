from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name_input = driver.find_element(By.NAME,"fName")
f_name_input.send_keys("Ruslan")

l_name_input = driver.find_element(By.NAME,"lName")
l_name_input.send_keys("Kapisaski")

email_input = driver.find_element(By.NAME,"email")
email_input.send_keys("haloobaloo@gmail.com")

button_submit = driver.find_element(By.TAG_NAME,"button")
button_submit.click()

driver.quit()