import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

service = Service('/usr/local/bin/geckodriver', service_args=['--profile-root=/tmp']) # muuda vastavalt oma süsteemile
options = Options()
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)

nime_vali = driver.find_element(By.ID, "username")
parooli_vali = driver.find_element(By.ID, "password")
submit_button = driver.find_element(By.TAG_NAME, "i")
time.sleep(1)
nime_vali.send_keys("tomsmith")
time.sleep(2)
parooli_vali.send_keys("SuperSecretPassword!")
time.sleep(1)
submit_button.click()
time.sleep(1)

tulemus = driver.find_element(By.ID, "flash")
print(tulemus.text)

input("Vajuta enter, et sulgeda..")

driver.quit()