import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver1 = webdriver.Chrome(executable_path="\\chromedriver_linux64")
driver1.get("https://www.rahulshettyacademy.com/AutomationPractice/")

# driver1.find_element(By.XPATH, "//input[@value='radio1']").click()

# txt = driver1.find_element(By.XPATH, "//legend[text()='Checkbox Example']").text
# print(txt)

# parent to child
# driver1.find_element(By.XPATH, "//label[@for='bmw']/input").click()

# driver1.find_element(By.XPATH, "//select[@id='dropdown-class-example']/option[2]").click()

# parent to last child
# driver1.find_element(By.XPATH, "//select[@id='dropdown-class-example']/option[last()]").click()

# grandparent to child
# s = driver1.find_element(By.XPATH, "//div[@class='block large-row-spacer']/div/fieldset/legend").text
# print(s)

# child to any ancestor
# driver1.find_element(By.XPATH, "//label[@for='radio3']/ancestor::div[@class='block large-row-spacer']")

# starts-with
driver1.find_element(By.XPATH, "//option[starts-with(@value,'opt')]").click()
time.sleep(20)