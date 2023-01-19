import pytest
from selenium import webdriver

from E_Shopper.PageObjects.LoginPage import Login


class Base:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="\\chromedriver_linux64")
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            print("Test is finished ")
            self.driver.close()
            self.driver.quit()

    def login_before_signup(self, driver):
        driver = self.driver
        login = Login(driver)
        login.click_to_login()
