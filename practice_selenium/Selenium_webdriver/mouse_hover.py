from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver1 = webdriver.Chrome(executable_path="\\chromedriver_linux64")
driver1.get("https://www.rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver1)
action.move_to_element(driver1.find_element(By.XPATH, "//button[@id='mousehover']")).perform()
action.move_to_element(driver1.find_element(By.XPATH, "//a[contains(text(),'Top')]")).click().perform()

