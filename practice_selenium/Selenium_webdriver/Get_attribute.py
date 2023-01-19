from selenium import webdriver
from selenium.webdriver.common.by import By

driver1 = webdriver.Chrome(executable_path="\\chromedriver_linux64")
driver1.implicitly_wait(10)
driver1.get("https://www.rahulshettyacademy.com/AutomationPractice/")
a = driver1.find_element(By.XPATH, "//input[@id='name']").get_attribute("placeholder")
print(a)
driver1.find_element(By.XPATH, "//input[@id='name']").send_keys("Nikita")
b = driver1.find_element(By.XPATH, "//input[@id='name']").get_attribute("value")
print(b)