from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from E_Shopper.Locators.locators import EShopLocators
from E_Shopper.PageObjects.LoginPage import Login


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.Create_account_link = EShopLocators.Create_account_link
        self.First_Name = EShopLocators.first_name
        self.Last_Name = EShopLocators.last_name
        self.Email = EShopLocators.Email
        self.Password = EShopLocators.password
        self.Signup_btn = EShopLocators.signup_submit

    def create_new_user(self):
        self.driver.find_element(By.XPATH, self.Create_account_link).click()

    def firstname_input(self, first_name):
        self.driver.find_element(By.XPATH, self.First_Name).send_keys(first_name)

    def lastname_input(self, last_name):
        self.driver.find_element(By.XPATH, self.Last_Name).send_keys(last_name)

    def email_input(self, email_field):
        self.driver.find_element(By.XPATH, self.Email).send_keys(email_field)

    def password_input(self, password):
        self.driver.find_element(By.XPATH, self.Password).send_keys(password)

    def signup_from_submit(self):
        self.driver.find_element(By.XPATH, self.Signup_btn).click()
