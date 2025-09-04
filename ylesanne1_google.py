import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.duckduckgo.com")
time.sleep(2)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("rasmo")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

input("Vajuta enter, et sulgeda..")

driver.quit()