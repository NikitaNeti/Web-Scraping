class EShopLocators:

    # Registration page
    Create_account_link = "//a[normalize-space()='Create Your Account']"
    first_name = "//input[@id='id_first_name']"
    last_name = "//input[@id='id_last_name']"
    Email = "//input[@id='id_email']"
    password = "//input[@id='id_password']"
    signup_submit = "//button[normalize-space()='Signup']"
    login_link = "//a[normalize-space()='Log In']"

    # login page
    login_btn_click = "//ul[@class='nav navbar-nav']//a[normalize-space()='Login']"
    email = "//input[@id='id_username']"
    password = "//input[@id='id_password']"
    login_submit = "//button[normalize-space()='Login']"
    logout_btn = "//a[normalize-space()='Logout']"
