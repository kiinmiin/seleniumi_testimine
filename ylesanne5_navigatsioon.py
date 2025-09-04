import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

service = Service('/usr/local/bin/geckodriver', service_args=['--profile-root=/tmp']) # muuda vastavalt oma süsteemile
options = Options()
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://the-internet.herokuapp.com")
time.sleep(2)

checkboxes = driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[6]/a")
checkboxes.click()
time.sleep(2)

checkbox1 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/input[1]")
checkbox1.click()
time.sleep(2)

driver.back()

input("Vajuta enter, et sulgeda..")

driver.quit()