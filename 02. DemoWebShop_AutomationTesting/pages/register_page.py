from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    gender_male = (By.CSS_SELECTOR, "#gender-male")
    gender_female = (By.ID, "gender-female")
    first_name = (By.XPATH, "//input[@id='FirstName']")
    last_name = (By.XPATH, "//input[@id='LastName']")
    email = (By.CSS_SELECTOR, "#Email")
    password = (By.ID, "Password")
    confirm_password = (By.ID, "ConfirmPassword")
    register_button = (By.XPATH, "//input[@id='register-button']")
    registration_success_message = (By.CSS_SELECTOR,".result")
    continue_button = (By.CSS_SELECTOR, "input[value='Continue']")

    def select_gender(self, gender):
        if gender.lower() == "male":
            self.wait.until(
                EC.element_to_be_clickable(self.gender_male)
            ).click()

        elif gender.lower() == "female":
            self.wait.until(
                EC.element_to_be_clickable(self.gender_female)
            ).click()

        else:
            raise ValueError("Gender must be 'male' or 'female'")

    def register(self, first_name, last_name, email, password):

        self.wait.until(
            EC.visibility_of_element_located(self.first_name)
        ).send_keys(first_name)

        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.confirm_password).send_keys(password)

        self.wait.until(
            EC.element_to_be_clickable(self.register_button)
        ).click()

    def is_registration_successful(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.registration_success_message
            )
        ).is_displayed()

    def click_continue(self):
        self.wait.until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()