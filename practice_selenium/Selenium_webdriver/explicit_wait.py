from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver1 = webdriver.Chrome(executable_path="\\chromedriver_linux64")
driver1.maximize_window()
# driver1.get("https://chercher.tech/practice/implicit-wait-example")
# WebDriverWait(driver1,10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@id='q']/input[1]")))
# driver1.find_element(By.XPATH, "//div[@id='q']/input[1]").click()

driver1.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
driver1.find_element(By.XPATH, "//button[@id='populate-text']").click()
WebDriverWait(driver1, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//h2[@id='h2']"),"Selenium Webdriver"))