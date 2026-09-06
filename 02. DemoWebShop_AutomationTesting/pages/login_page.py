from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    email = (By.ID, "Email")
    password = (By.ID, "Password")
    login_button = (By.XPATH, "(//input[@value='Log in'])[1]")
    logout_button = (By.CSS_SELECTOR, ".ico-logout")
    login_error = (By.CSS_SELECTOR,".validation-summary-errors")

    def enter_email(self, email):
        self.wait.until(
            EC.visibility_of_element_located(self.email)).send_keys(email)



    def enter_password(self, password):
        self.wait.until(
            EC.visibility_of_element_located(self.password)).send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.login_button)).click()

    def is_logged_in(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.logout_button)
        ).is_displayed()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def is_login_error_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.login_error)
        ).is_displayed()