import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com")
time.sleep(2)
#search_box = driver.find_element(By.NAME, "q")
#search_box.send_keys(Keys.RETURN)
#time.sleep(2)
quotes = driver.find_elements(By.CLASS_NAME, "text")
authors = driver.find_elements(By.CLASS_NAME, "author")

for quote, author in zip(quotes, authors):
    print(f"{quote.text} - {author.text}")

time.sleep(3)

input("Vajuta enter, et sulgeda..")

driver.quit()