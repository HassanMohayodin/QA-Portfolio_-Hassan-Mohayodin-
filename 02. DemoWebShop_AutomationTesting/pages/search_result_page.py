from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    product_items = (By.CSS_SELECTOR, ".product-item")
    no_results_message = (By.XPATH, "//strong[@class='result']")
    product_links = (By.CSS_SELECTOR, ".product-item .product-title a")

    def get_product_count(self):
        products = self.wait.until(
            EC.presence_of_all_elements_located(self.product_items)
        )

        return len(products)

    def is_no_results_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.no_results_message
            )
        ).is_displayed()

    def open_product(self, product_name):

        product_locator = (
            By.XPATH,
            f"//a[normalize-space()='{product_name}']"
        )

        def click_product(driver):
            try:
                element = driver.find_element(*product_locator)

                if element.is_displayed() and element.is_enabled():
                    element.click()
                    return True

            except Exception:
                return False

            return False

        self.wait.until(click_product)