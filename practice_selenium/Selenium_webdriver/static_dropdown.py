import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver1 = webdriver.Chrome(executable_path="\\chromedriver_linux64")
driver1.get("https://www.rahulshettyacademy.com/AutomationPractice/")
static_dropdown = Select(driver1.find_element(By.XPATH, "//select[@id='dropdown-class-example']"))
static_dropdown.select_by_visible_text('Option3')
time.sleep(2)
static_dropdown.select_by_index(2)
time.sleep(2)
static_dropdown.select_by_value('option1')
time.sleep(2)
