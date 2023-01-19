from selenium import webdriver
from selenium.webdriver.common.by import By

driver1 = webdriver.Chrome(executable_path="\\chromedriver_linux64")
driver1.get("https://chercher.tech/practice/implicit-wait-example")
driver1.implicitly_wait(30)
driver1.find_element(By.XPATH, "//div[@id='q']/input[1]").click()
driver1.find_element(By.XPATH, "//div[@id='q']/input[3]").click()