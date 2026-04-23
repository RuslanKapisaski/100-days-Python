from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

# Add driver
driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS?th=1")
driver.get("https://www.python.org/")

# Finding elements by CLASS
# price_dollar = driver.find_element(By.CLASS_NAME,"a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME,"a-price-fraction")

# Finding elements by ID
search_bar = driver.find_element(By.NAME,value="q")
submit_button = driver.find_element(By.ID,value="submit")

# Finding elements by CSS selector
documentation_link = driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")

# Finding elements by XPATH
learn_more_link= driver.find_element(By.XPATH,value='//*[@id="touchnav-wrapper"]/header/div/div[4]/p/a')
print(learn_more_link.text)

# Printing website elements
# print(f"The price is {price_dollar.text}.{price_cents.text}")
# print(search_bar)
# print(search_bar.get_attribute("placeholder"))
# print(submit_button.size)
# print(documentation_link.text)

#Closes particular tab
# driver.close()


#Closes the entire browser
driver.quit()

