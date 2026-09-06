from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    checkout_as_guest_button = (
        By.CSS_SELECTOR,
        "input[value='Checkout as Guest']"
    )

    billing_first_name = (
        By.CSS_SELECTOR,
        "#BillingNewAddress_FirstName"
    )

    last_name = (
        By.CSS_SELECTOR,
        "#BillingNewAddress_LastName"
    )

    email = (
        By.CSS_SELECTOR,
        "#BillingNewAddress_Email"
    )

    company = (
        By.CSS_SELECTOR,
        "#BillingNewAddress_Company"
    )

    country = (
        By.CSS_SELECTOR,
        "#BillingNewAddress_CountryId"
    )

    city = (
        By.CSS_SELECTOR,
        "#BillingNewAddress_City"
    )

    address = (
        By.CSS_SELECTOR,
        "#BillingNewAddress_Address1"
    )

    zip_code = (
        By.CSS_SELECTOR,
        "#BillingNewAddress_ZipPostalCode"
    )

    phone = (
        By.CSS_SELECTOR,
        "#BillingNewAddress_PhoneNumber"
    )

    continue_button = (
        By.CSS_SELECTOR,
        "input[onclick='Billing.save()']"
    )

    shipping_address = (
        By.CSS_SELECTOR,
        "#shipping-address-select"
    )

    shipping_first_name = (
        By.CSS_SELECTOR,
        "#ShippingNewAddress_FirstName"
    )

    shipping_last_name = (
        By.CSS_SELECTOR,
        "#ShippingNewAddress_LastName"
    )

    shipping_email = (
        By.CSS_SELECTOR,
        "#ShippingNewAddress_Email"
    )

    shipping_country = (
        By.CSS_SELECTOR,
        "#ShippingNewAddress_CountryId"
    )

    shipping_city = (
        By.CSS_SELECTOR,
        "#ShippingNewAddress_City"
    )

    shipping_address_field = (
        By.CSS_SELECTOR,
        "#ShippingNewAddress_Address1"
    )

    shipping_zip_code = (
        By.CSS_SELECTOR,
        "#ShippingNewAddress_ZipPostalCode"
    )

    shipping_phone = (
        By.CSS_SELECTOR,
        "#ShippingNewAddress_PhoneNumber"
    )

    shipping_continue_button = (
        By.CSS_SELECTOR,
        "input[onclick='Shipping.save()']"
    )

    shipping_ground = (
        By.CSS_SELECTOR,
        "#shippingoption_0"
    )

    shipping_next_day = (
        By.CSS_SELECTOR,
        "#shippingoption_1"
    )

    shipping_second_day = (
        By.CSS_SELECTOR,
        "#shippingoption_2"
    )

    shipping_method_continue = (
        By.CSS_SELECTOR,
        "input[class='button-1 shipping-method-next-step-button']"
    )

    payment_cod = (
        By.CSS_SELECTOR,
        "#paymentmethod_0"
    )

    payment_check = (
        By.CSS_SELECTOR,
        "#paymentmethod_1"
    )

    payment_credit_card = (
        By.CSS_SELECTOR,
        "#paymentmethod_2"
    )

    payment_purchase_order = (
        By.CSS_SELECTOR,
        "#paymentmethod_3"
    )

    payment_method_continue = (
        By.CSS_SELECTOR,
        "input[class='button-1 payment-method-next-step-button']"
    )

    payment_info_continue_button = (
        By.CSS_SELECTOR,
        "input[class='button-1 payment-info-next-step-button']"
    )

    confirm_order_button = (
        By.CSS_SELECTOR,
        "input[value='Confirm']"
    )

    order_complete_continue_button = (
        By.CSS_SELECTOR,
        "input[value='Continue']"
    )

    order_success_message = (
        By.XPATH,
        "//strong[normalize-space()='Your order has been successfully processed!']"
    )

    #Validation
    first_name_error = (
        By.XPATH,
        "//span[@class='field-validation-error' and normalize-space()='First name is required.']"
    )

    last_name_error = (
        By.CSS_SELECTOR,
        ".field-validation-error[data-valmsg-for='BillingNewAddress.LastName']"
    )

    email_error = (
        By.XPATH,
        "//span[normalize-space()='Email is required.']"
    )

    invalid_email = (By.XPATH,"//span[normalize-space()='Wrong email']")

    country_error = (
        By.XPATH,
        "//span[normalize-space()='Country is required.']"
    )

    city_error = (
        By.CSS_SELECTOR,
        ".field-validation-error[data-valmsg-for='BillingNewAddress.City']"
    )

    address_error = (
        By.XPATH,
        "//span[normalize-space()='Street address is required']"
    )

    zip_code_error = (
        By.CSS_SELECTOR,
        ".field-validation-error[data-valmsg-for='BillingNewAddress.ZipPostalCode']"
    )

    phone_error = (
        By.XPATH,
        "//span[normalize-space()='Phone is required']"
    )

    zip_error = (
        By.CSS_SELECTOR,
        ".field-validation-error[data-valmsg-for='BillingNewAddress.ZipPostalCode']"
    )

    shipping_first_name_error = (
        By.CSS_SELECTOR,
        ".field-validation-error[data-valmsg-for='ShippingNewAddress.FirstName']"
    )

    shipping_last_name_error = (
        By.CSS_SELECTOR,
        ".field-validation-error[data-valmsg-for='ShippingNewAddress.LastName']"
    )

    shipping_email_error = (
        By.CSS_SELECTOR,
        ".field-validation-error[data-valmsg-for='ShippingNewAddress.Email']"
    )

    shipping_country_error = (
        By.CSS_SELECTOR,
        ".field-validation-error[data-valmsg-for='ShippingNewAddress.CountryId']"
    )

    shipping_city_error = (
        By.CSS_SELECTOR,
        ".field-validation-error[data-valmsg-for='ShippingNewAddress.City']"
    )

    shipping_address_error = (
        By.CSS_SELECTOR,
        ".field-validation-error[data-valmsg-for='ShippingNewAddress.Address1']"
    )

    shipping_zip_error = (
        By.CSS_SELECTOR,
        ".field-validation-error[data-valmsg-for='ShippingNewAddress.ZipPostalCode']"
    )

    shipping_phone_error = (
        By.CSS_SELECTOR,
        ".field-validation-error[data-valmsg-for='ShippingNewAddress.PhoneNumber']"
    )

    def checkout_as_guest(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.checkout_as_guest_button
            )
        ).click()

    def is_checkout_page_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.billing_first_name
            )
        ).is_displayed()

    def enter_first_name(self, billing_first_name):
        self.wait.until(
            EC.visibility_of_element_located(self.billing_first_name)
        ).send_keys(billing_first_name)

    def enter_last_name(self, last_name):
        self.wait.until(
            EC.visibility_of_element_located(self.last_name)
        ).send_keys(last_name)

    def enter_email(self, email):
        self.wait.until(
            EC.visibility_of_element_located(self.email)
        ).send_keys(email)

    def enter_company(self, company):
        self.wait.until(
            EC.visibility_of_element_located(self.company)
        ).send_keys(company)

    def select_country(self, country):
        country_dropdown = self.wait.until(
            EC.visibility_of_element_located(self.country)
        )

        Select(country_dropdown).select_by_visible_text(country)

    def enter_city(self, city):
        self.wait.until(
            EC.visibility_of_element_located(self.city)
        ).send_keys(city)

    def enter_address(self, address):
        self.wait.until(
            EC.visibility_of_element_located(self.address)
        ).send_keys(address)

    def enter_zip_code(self, zip_code):
        self.wait.until(
            EC.visibility_of_element_located(self.zip_code)
        ).send_keys(zip_code)

    def enter_phone(self, phone):
        self.wait.until(
            EC.visibility_of_element_located(self.phone)
        ).send_keys(phone)

    def continue_billing(self):
        self.wait.until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()

    def select_shipping_address(self, address):
        shipping_dropdown = self.wait.until(
            EC.visibility_of_element_located(self.shipping_address)
        )

        Select(shipping_dropdown).select_by_visible_text(address)


    def select_new_shipping_address(self):
        shipping_dropdown = self.wait.until(
            EC.visibility_of_element_located(
                self.shipping_address
            )
        )

        Select(shipping_dropdown).select_by_visible_text(
            "New Address"
        )

    def enter_shipping_first_name(self, first_name):
        self.wait.until(
            EC.visibility_of_element_located(
                self.shipping_first_name
            )
        ).send_keys(first_name)

    def enter_shipping_last_name(self, last_name):
        self.wait.until(
            EC.visibility_of_element_located(
                self.shipping_last_name
            )
        ).send_keys(last_name)

    def enter_shipping_email(self, email):
        self.wait.until(
            EC.visibility_of_element_located(
                self.shipping_email
            )
        ).send_keys(email)

    def select_shipping_country(self, country):
        country_dropdown = self.wait.until(
            EC.visibility_of_element_located(
                self.shipping_country
            )
        )

        Select(country_dropdown).select_by_visible_text(
            country
        )

    def enter_shipping_city(self, city):
        self.wait.until(
            EC.visibility_of_element_located(
                self.shipping_city
            )
        ).send_keys(city)

    def enter_shipping_address(self, address):
        self.wait.until(
            EC.visibility_of_element_located(
                self.shipping_address_field
            )
        ).send_keys(address)

    def enter_shipping_zip_code(self, zip_code):
        self.wait.until(
            EC.visibility_of_element_located(
                self.shipping_zip_code
            )
        ).send_keys(zip_code)

    def enter_shipping_phone(self, phone):
        self.wait.until(
            EC.visibility_of_element_located(
                self.shipping_phone
            )
        ).send_keys(phone)

    def continue_shipping_address(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.shipping_continue_button
            )
        ).click()

    def select_ground_shipping(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.shipping_ground
            )
        ).click()

    def continue_shipping_method(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.shipping_method_continue
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.payment_cod
            )
        )

    def select_cash_on_delivery(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.payment_cod
            )
        ).click()

    def continue_payment_method(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.payment_method_continue
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.payment_info_continue_button
            )
        )

    def continue_payment_information(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.payment_info_continue_button
            )
        ).click()

        self.wait.until(
            EC.visibility_of_element_located(
                self.confirm_order_button
            )
        )

    def confirm_order(self):
        self.wait.until(
            EC.element_to_be_clickable(self.confirm_order_button)
        ).click()

    def is_order_placed(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.order_success_message
            )
        ).is_displayed()

    def continue_after_order(self):
        self.wait.until(
            EC.element_to_be_clickable(
                self.order_complete_continue_button
            )
        ).click()

#Validation
    def is_first_name_error_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.first_name_error
            )
        ).is_displayed()

    def is_validation_error_displayed(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).is_displayed()

    def select_next_day_shipping(self):
        self.wait.until(
            EC.element_to_be_clickable(self.shipping_next_day)
        ).click()

    def select_second_day_shipping(self):
        self.wait.until(
            EC.element_to_be_clickable(self.shipping_second_day)
        ).click()

    def is_payment_method_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.payment_cod
            )
        ).is_displayed()

    def is_payment_information_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.payment_info_continue_button
            )
        ).is_displayed()

    def is_confirm_order_displayed(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.confirm_order_button
            )
        ).is_displayed()