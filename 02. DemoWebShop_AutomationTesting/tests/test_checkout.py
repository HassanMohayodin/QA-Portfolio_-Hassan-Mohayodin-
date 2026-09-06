import pytest

import pytest

pytestmark = pytest.mark.checkout

@pytest.mark.smoke
@pytest.mark.regression
def test_guest_checkout(checkout_page):

    checkout_page.enter_first_name("Hassan")
    checkout_page.enter_last_name("Demo")
    checkout_page.enter_email("hassandemo@example.com")

    checkout_page.select_country("United States")

    checkout_page.enter_city("New York")
    checkout_page.enter_address("123 Test Street")
    checkout_page.enter_zip_code("10001")
    checkout_page.enter_phone("1234567890")

    checkout_page.continue_billing()

    checkout_page.select_new_shipping_address()

    checkout_page.enter_shipping_first_name("Hassan")
    checkout_page.enter_shipping_last_name("Demo")
    checkout_page.enter_shipping_email("hassandemo@example.com")

    checkout_page.select_shipping_country("United States")

    checkout_page.enter_shipping_city("New York")
    checkout_page.enter_shipping_address("123 Test Street")
    checkout_page.enter_shipping_zip_code("10001")
    checkout_page.enter_shipping_phone("1234567890")

    checkout_page.continue_shipping_address()

    checkout_page.select_ground_shipping()
    checkout_page.continue_shipping_method()

    checkout_page.select_cash_on_delivery()
    checkout_page.continue_payment_method()

    checkout_page.continue_payment_information()

    checkout_page.confirm_order()

    assert checkout_page.is_order_placed()

    checkout_page.continue_after_order()


def test_checkout_page_loads(checkout_page):

    assert checkout_page.is_checkout_page_displayed()

def test_select_ground_shipping(checkout_page):

    # Billing
    checkout_page.enter_first_name("Hassan")
    checkout_page.enter_last_name("Demo")
    checkout_page.enter_email("hassandemo@example.com")
    checkout_page.select_country("United States")
    checkout_page.enter_city("New York")
    checkout_page.enter_address("123 Test Street")
    checkout_page.enter_zip_code("10001")
    checkout_page.enter_phone("1234567890")

    checkout_page.continue_billing()

    # Shipping Address
    checkout_page.select_new_shipping_address()
    checkout_page.enter_shipping_first_name("Hassan")
    checkout_page.enter_shipping_last_name("Demo")
    checkout_page.enter_shipping_email("hassandemo@example.com")
    checkout_page.select_shipping_country("United States")
    checkout_page.enter_shipping_city("New York")
    checkout_page.enter_shipping_address("123 Test Street")
    checkout_page.enter_shipping_zip_code("10001")
    checkout_page.enter_shipping_phone("1234567890")

    checkout_page.continue_shipping_address()

    # Shipping Method
    checkout_page.select_ground_shipping()
    checkout_page.continue_shipping_method()

    # Verify we reached Payment Method
    assert checkout_page.is_payment_method_displayed()

def test_select_next_day_shipping(checkout_page):

    checkout_page.enter_first_name("Hassan")
    checkout_page.enter_last_name("Demo")
    checkout_page.enter_email("hassandemo@example.com")

    checkout_page.select_country("United States")
    checkout_page.enter_city("New York")
    checkout_page.enter_address("123 Test Street")
    checkout_page.enter_zip_code("10001")
    checkout_page.enter_phone("1234567890")

    checkout_page.continue_billing()

    checkout_page.select_new_shipping_address()

    checkout_page.enter_shipping_first_name("Hassan")
    checkout_page.enter_shipping_last_name("Demo")
    checkout_page.enter_shipping_email("hassandemo@example.com")
    checkout_page.select_shipping_country("United States")
    checkout_page.enter_shipping_city("New York")
    checkout_page.enter_shipping_address("123 Test Street")
    checkout_page.enter_shipping_zip_code("10001")
    checkout_page.enter_shipping_phone("1234567890")

    checkout_page.continue_shipping_address()

    checkout_page.select_next_day_shipping()
    checkout_page.continue_shipping_method()

    assert checkout_page.is_payment_method_displayed()


def test_select_second_day_shipping(checkout_page):

    checkout_page.enter_first_name("Hassan")
    checkout_page.enter_last_name("Demo")
    checkout_page.enter_email("hassandemo@example.com")

    checkout_page.select_country("United States")
    checkout_page.enter_city("New York")
    checkout_page.enter_address("123 Test Street")
    checkout_page.enter_zip_code("10001")
    checkout_page.enter_phone("1234567890")

    checkout_page.continue_billing()

    checkout_page.select_new_shipping_address()

    checkout_page.enter_shipping_first_name("Hassan")
    checkout_page.enter_shipping_last_name("Demo")
    checkout_page.enter_shipping_email("hassandemo@example.com")
    checkout_page.select_shipping_country("United States")
    checkout_page.enter_shipping_city("New York")
    checkout_page.enter_shipping_address("123 Test Street")
    checkout_page.enter_shipping_zip_code("10001")
    checkout_page.enter_shipping_phone("1234567890")

    checkout_page.continue_shipping_address()

    checkout_page.select_second_day_shipping()
    checkout_page.continue_shipping_method()

    assert checkout_page.is_payment_method_displayed()

def test_select_cash_on_delivery(checkout_page):

    # Billing
    checkout_page.enter_first_name("Hassan")
    checkout_page.enter_last_name("Demo")
    checkout_page.enter_email("hassandemo@example.com")
    checkout_page.select_country("United States")
    checkout_page.enter_city("New York")
    checkout_page.enter_address("123 Test Street")
    checkout_page.enter_zip_code("10001")
    checkout_page.enter_phone("1234567890")

    checkout_page.continue_billing()

    # Shipping Address
    checkout_page.select_new_shipping_address()
    checkout_page.enter_shipping_first_name("Hassan")
    checkout_page.enter_shipping_last_name("Demo")
    checkout_page.enter_shipping_email("hassandemo@example.com")
    checkout_page.select_shipping_country("United States")
    checkout_page.enter_shipping_city("New York")
    checkout_page.enter_shipping_address("123 Test Street")
    checkout_page.enter_shipping_zip_code("10001")
    checkout_page.enter_shipping_phone("1234567890")

    checkout_page.continue_shipping_address()

    # Shipping Method
    checkout_page.select_ground_shipping()
    checkout_page.continue_shipping_method()

    # Payment Method
    checkout_page.select_cash_on_delivery()
    checkout_page.continue_payment_method()

    # Verify Payment Information step
    assert checkout_page.is_payment_information_displayed()

def test_cash_on_delivery_payment_information(checkout_page):

    # Billing
    checkout_page.enter_first_name("Hassan")
    checkout_page.enter_last_name("Demo")
    checkout_page.enter_email("hassandemo@example.com")
    checkout_page.select_country("United States")
    checkout_page.enter_city("New York")
    checkout_page.enter_address("123 Test Street")
    checkout_page.enter_zip_code("10001")
    checkout_page.enter_phone("1234567890")

    checkout_page.continue_billing()

    # Shipping Address
    checkout_page.select_new_shipping_address()
    checkout_page.enter_shipping_first_name("Hassan")
    checkout_page.enter_shipping_last_name("Demo")
    checkout_page.enter_shipping_email("hassandemo@example.com")
    checkout_page.select_shipping_country("United States")
    checkout_page.enter_shipping_city("New York")
    checkout_page.enter_shipping_address("123 Test Street")
    checkout_page.enter_shipping_zip_code("10001")
    checkout_page.enter_shipping_phone("1234567890")

    checkout_page.continue_shipping_address()

    # Shipping Method
    checkout_page.select_ground_shipping()
    checkout_page.continue_shipping_method()

    # Payment Method
    checkout_page.select_cash_on_delivery()
    checkout_page.continue_payment_method()

    # Payment Information
    checkout_page.continue_payment_information()

    # Verify Confirm Order button is displayed
    assert checkout_page.is_confirm_order_displayed()

def test_confirm_order(checkout_page):

    # Billing
    checkout_page.enter_first_name("Hassan")
    checkout_page.enter_last_name("Demo")
    checkout_page.enter_email("hassandemo@example.com")
    checkout_page.select_country("United States")
    checkout_page.enter_city("New York")
    checkout_page.enter_address("123 Test Street")
    checkout_page.enter_zip_code("10001")
    checkout_page.enter_phone("1234567890")

    checkout_page.continue_billing()

    # Shipping Address
    checkout_page.select_new_shipping_address()
    checkout_page.enter_shipping_first_name("Hassan")
    checkout_page.enter_shipping_last_name("Demo")
    checkout_page.enter_shipping_email("hassandemo@example.com")
    checkout_page.select_shipping_country("United States")
    checkout_page.enter_shipping_city("New York")
    checkout_page.enter_shipping_address("123 Test Street")
    checkout_page.enter_shipping_zip_code("10001")
    checkout_page.enter_shipping_phone("1234567890")

    checkout_page.continue_shipping_address()

    # Shipping Method
    checkout_page.select_ground_shipping()
    checkout_page.continue_shipping_method()

    # Payment Method
    checkout_page.select_cash_on_delivery()
    checkout_page.continue_payment_method()

    # Payment Information
    checkout_page.continue_payment_information()

    # Confirm Order
    checkout_page.confirm_order()

    # Verify successful order
    assert checkout_page.is_order_placed()

def test_order_success_continue(checkout_page):

    # Billing
    checkout_page.enter_first_name("Hassan")
    checkout_page.enter_last_name("Demo")
    checkout_page.enter_email("hassandemo@example.com")
    checkout_page.select_country("United States")
    checkout_page.enter_city("New York")
    checkout_page.enter_address("123 Test Street")
    checkout_page.enter_zip_code("10001")
    checkout_page.enter_phone("1234567890")

    checkout_page.continue_billing()

    # Shipping Address
    checkout_page.select_new_shipping_address()
    checkout_page.enter_shipping_first_name("Hassan")
    checkout_page.enter_shipping_last_name("Demo")
    checkout_page.enter_shipping_email("hassandemo@example.com")
    checkout_page.select_shipping_country("United States")
    checkout_page.enter_shipping_city("New York")
    checkout_page.enter_shipping_address("123 Test Street")
    checkout_page.enter_shipping_zip_code("10001")
    checkout_page.enter_shipping_phone("1234567890")

    checkout_page.continue_shipping_address()

    # Shipping Method
    checkout_page.select_ground_shipping()
    checkout_page.continue_shipping_method()

    # Payment Method
    checkout_page.select_cash_on_delivery()
    checkout_page.continue_payment_method()

    # Payment Information
    checkout_page.continue_payment_information()

    # Confirm Order
    checkout_page.confirm_order()

    assert checkout_page.is_order_placed()

    # Continue after successful order
    checkout_page.continue_after_order()