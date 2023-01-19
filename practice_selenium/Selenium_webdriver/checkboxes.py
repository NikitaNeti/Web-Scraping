import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver1 = webdriver.Chrome(executable_path="\\chromedriver_linux64")
driver1.get("https://www.rahulshettyacademy.com/AutomationPractice/")
check = driver1.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in check:
    if checkbox == check[1]:
        pass
    else:
        checkbox.click()

time.sleep(15)