from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='\\chromedriver_linux64')
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# ID
# a = driver.find_element(By.ID, "input")
# a.send_keys("Nikita")
#
# a = driver.find_element(By.ID, "alertbtn")
# a.click()

# CLASS_NAME
# a = driver.find_element(By.CLASS_NAME, "inputs")
# a.send_keys("Nikita")

# NAME
# a = driver.find_element(By.NAME, "enter-name")
# a.send_keys("Nikita")

# LINK_TEXT
# driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()

# LINK_TEXT
# driver.find_element(By.PARTIAL_LINK_TEXT, "Access ").click()

# TAG_NAME
# b = driver.find_element(By.TAG_NAME, 'h1').text
# print(b)

# CSS selector
driver.find_element(By.CSS_SELECTOR, "input[value='radio1']").click()

driver.find_element(By.CSS_SELECTOR, "#name").send_keys('niki')


time.sleep(20)
