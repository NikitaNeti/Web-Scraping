import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver1 = webdriver.Chrome(executable_path="\\chromedriver_linux64")
driver1.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver1.find_element(By.XPATH, "//input[@id='name']").send_keys('Nikita')
time.sleep(2)
driver1.find_element(By.XPATH, "//input[@id='alertbtn']").click()
# driver1.find_element(By.XPATH, "//input[@id='confirmbtn']").click()
# time.sleep(2)
alert = driver1.switch_to.alert
time.sleep(2)
assert 'Nikita' in alert.text
alert.accept()
# alert.dismiss()
# print(alert.text)
