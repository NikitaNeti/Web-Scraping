from selenium import webdriver
from selenium.webdriver.common.by import By

driver1 = webdriver.Chrome(executable_path="\\chromedriver_linux64")
driver1.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver1.find_element(By.XPATH, "//button[@id='openwindow']").click()
# print(driver1.window_handles)
driver1.switch_to.window(driver1.window_handles[1])
driver1.find_element(By.XPATH, "//a[normalize-space()='Practice']").click()
# driver1.switch_to.window(driver1.window_handles[0])


