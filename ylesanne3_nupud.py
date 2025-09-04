import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
time.sleep(2)

nupp = driver.find_element(By.TAG_NAME, "button")
nupp.click()
nupp.click()
time.sleep(2)
nupp.click()
nupp.click()
nupp.click()
time.sleep(3)


while True:
    delete_nupp = driver.find_elements(By.CLASS_NAME, "added-manually")

    if not delete_nupp:
        break

    delete_nupp[0].click()
    time.sleep(0.2) 

time.sleep(2)
input("Vajuta enter, et sulgeda..")

driver.quit()