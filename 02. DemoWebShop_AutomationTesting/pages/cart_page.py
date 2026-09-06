from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    cart_link = (By.CSS_SELECTOR, "li[id='topcartlink'] a[class='ico-cart']")
    product_name = (By.CSS_SELECTOR, ".product-name")
    quantity = (By.CLASS_NAME, "qty-input")
    unit_price = (By.CSS_SELECTOR, ".product-unit-price")
    total_price = (By.CSS_SELECTOR, ".product-subtotal")
    remove_checkbox = (By.XPATH, "//input[@name='removefromcart']")
    update_cart_button = (By.CSS_SELECTOR, "input[value='Update shopping cart']")
    empty_cart_message = (
        By.XPATH,
        "//div[@class='order-summary-content']"
    )
    cart_notification = (
        By.CSS_SELECTOR,
        "#bar-notification"
    )

    terms_checkbox = (By.CSS_SELECTOR, "#termsofservice")
    checkout_button = (By.CSS_SELECTOR, "#checkout")

    def open_cart(self):
        self.wait.until(
            EC.invisibility_of_element_located(self.cart_notification)
        )

        self.wait.until(
            EC.element_to_be_clickable(self.cart_link)
        ).click()

    def get_product_name(self):
        product = self.wait.until(
            EC.presence_of_element_located(self.product_name)
        )
        return product.text.strip()

    def get_quantity(self):
        quantity = self.wait.until(
            EC.visibility_of_element_located(self.quantity)
        )
        return quantity.get_attribute("value")

    def get_unit_price(self):
        price = self.wait.until(
            EC.visibility_of_element_located(self.unit_price)
        )
        return price.text.strip()

    def get_total_price(self):
        total = self.wait.until(
            EC.visibility_of_element_located(self.total_price)
        )
        return total.text.strip()

    def set_quantity(self, quantity):
        quantity_field = self.wait.until(
            EC.visibility_of_element_located(self.quantity)
        )
        quantity_field.clear()
        quantity_field.send_keys(str(quantity))


    def remove_product(self):
        self.wait.until(
            EC.element_to_be_clickable(self.remove_checkbox)
        ).click()


    def update_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.update_cart_button)
        ).click()

    def is_cart_empty(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.empty_cart_message
            )
        ).is_displayed()

    def agree_to_terms(self):
        self.wait.until(
            EC.element_to_be_clickable(self.terms_checkbox)
        ).click()

    def checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()