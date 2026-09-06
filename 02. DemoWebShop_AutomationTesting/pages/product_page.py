from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    product_title = (By.CSS_SELECTOR, ".product-name")
    add_to_cart_button = (By.XPATH, "//input[@id='add-to-cart-button-72']")
    cart_notification = (
        By.CSS_SELECTOR,
        "#bar-notification"
    )

    def get_product_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.product_title)
        ).text

    def add_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(self.cart_notification)
        )

    def is_product_added_to_cart(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.cart_notification
            )
        ).is_displayed()