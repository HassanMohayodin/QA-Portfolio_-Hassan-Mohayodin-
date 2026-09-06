from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    search_box = (By.XPATH, "//input[@id='small-searchterms']")
    search_button = (By.CSS_SELECTOR, "input[value='Search']")


    def search(self, search_term):
        self.wait.until(
            EC.visibility_of_element_located(self.search_box)
        ).send_keys(search_term)

        self.wait.until(
            EC.element_to_be_clickable(self.search_button)
        ).click()