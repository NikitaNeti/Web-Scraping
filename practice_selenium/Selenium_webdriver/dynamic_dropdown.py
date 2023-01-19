import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver1 = webdriver.Chrome(executable_path="\\chromedriver_linux64")
driver1.get("https://www.indianrail.gov.in/enquiry/TBIS/TrainBetweenImportantStations.html")
driver1.find_element(By.ID, "sourceStation").send_keys('BHO')
time.sleep(2)
driver1.maximize_window()
from_airport = driver1.find_elements(By.XPATH, "//ul[@id='ui-id-1']/li/a")
for airport in from_airport:
    if airport.text == "BHODWAL MAJRI - BDMJ":
        airport.click()
        time.sleep(50)
    else:
        pass


