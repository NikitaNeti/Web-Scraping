from selenium import webdriver
from selenium.webdriver.common.by import By

driver1 = webdriver.Chrome(executable_path="\\chromedriver_linux64")
driver1.implicitly_wait(10)
driver1.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver1.switch_to.frame(driver1.find_element(By.XPATH, "//iframe[@id='courses-iframe']"))
driver1.find_element(By.XPATH, "//div[@class='nav-outer clearfix']//a[normalize-space()='Job Support']").click()
driver1.switch_to.default_content()
driver1.find_element(By.XPATH, "//input[@id='checkBoxOption1']").click()
