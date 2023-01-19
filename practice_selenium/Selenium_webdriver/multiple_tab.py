from selenium import webdriver
from selenium.webdriver.common.by import By

driver1 = webdriver.Chrome(executable_path="\\chromedriver_linux64")
driver1.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver1.find_element(By.XPATH, "//a[@id='opentab']").click()
tab = driver1.window_handles[1]
driver1.find_element(By.XPATH, "//button[@id='openwindow']").click()
window2 = driver1.window_handles[2]
driver1.switch_to.window(tab)
driver1.find_element(By.XPATH, "//div[@class='nav-outer clearfix']//nav[@class='main-menu']//div[@class='navbar-collapse collapse clearfix']//ul[@class='navigation clearfix']//li//a[@href='practice-project'][normalize-space()='Practice']").click()
driver1.switch_to.window(window2)
driver1.find_element(By.XPATH, "//a[normalize-space()='Practice']").click()