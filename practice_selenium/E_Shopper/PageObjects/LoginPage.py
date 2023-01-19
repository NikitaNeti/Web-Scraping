from selenium import webdriver
from selenium.webdriver.common.by import By
from E_Shopper.Locators.locators import EShopLocators


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.Login_btn_click = EShopLocators.login_btn_click
        self.email_textbox = EShopLocators.email
        self.password_textbox = EShopLocators.password
        self.login_submit = EShopLocators.login_submit
        self.logout_btn = EShopLocators.logout_btn

    def click_to_login(self):
        self.driver.find_element(By.XPATH, self.Login_btn_click).click()

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email_textbox).clear()
        self.driver.find_element(By.XPATH,self.email_textbox).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_textbox).clear()
        self.driver.find_element(By.XPATH, self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_submit).click()

    def logout(self):
        self.driver.find_element(By.XPATH, self.logout_btn).click()

