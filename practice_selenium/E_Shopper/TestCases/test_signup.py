import time
import pytest
from selenium.webdriver.common.by import By
from E_Shopper.PageObjects.Registration import RegistrationPage
from E_Shopper.TestCases.base import Base


@pytest.mark.usefixtures('setup')
class TestSignup(Base):
    def test_sign(self):
        driver = self.driver
        self.login_before_signup(driver)
        time.sleep(3)
        signup = RegistrationPage(driver)
        signup.create_new_user()
        signup.firstname_input("Nikita")
        signup.lastname_input("Neti")
        signup.email_input("niki19@gmail.com")
        signup.password_input("admin@123")
        signup.signup_from_submit()
        time.sleep(10)
        assert driver.find_element(By.XPATH, "//span[normalize-space()='Already have an account']").text == "Already " \
                                                                                                            "have an " \
                                                                                                            "account"
        assert driver.find_element(By.XPATH, "//a[normalize-space()='Log In']").is_displayed
        assert "Home | E-Shopper" == driver.title
