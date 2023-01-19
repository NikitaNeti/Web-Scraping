from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver1 = webdriver.Chrome(executable_path="\\chromedriver_linux64")
driver1.get("https://the-internet.herokuapp.com/context_menu")

action = ActionChains(driver1)
# action.context_click(driver1.find_element(By.XPATH, "//div[@id='hot-spot']")).perform()
action.double_click(driver1.find_element(By.XPATH, "//div[@id='hot-spot']")).perform()