import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="\\chromedriver_linux64")
driver.get("http://127.0.0.1:8000/")
driver.maximize_window()
driver.find_element(By.XPATH ,"//ul[@class='nav navbar-nav']//a[normalize-space()='Login']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//a[normalize-space()='Create Your Account']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@id='id_first_name']").send_keys('Nikita')
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='id_last_name']").send_keys('neti')
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='id_email']").send_keys('nikitaneti19@gmail.com')
time.sleep(2)
# driver.find_element(By.XPATH, "//input[@id='id_password']").send_keys('nikita19@')
# time.sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Signup']").click()
time.sleep(2)