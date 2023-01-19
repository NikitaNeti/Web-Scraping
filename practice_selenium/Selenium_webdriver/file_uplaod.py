from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver1 = webdriver.Chrome(executable_path="\\chromedriver_linux64")
driver1.get("https://the-internet.herokuapp.com/upload")
driver1.find_element(By.XPATH, "//input[@id='file-upload']").send_keys("/home/neosoft/Downloads/rafting.jpg")
driver1.find_element(By.XPATH, "//input[@id='file-submit']").click()
time.sleep(20)