import pytest

@pytest.mark.validation
def test_billing_country_required(checkout_page):

    checkout_page.enter_first_name("Demo")
    checkout_page.enter_last_name("Demo")
    checkout_page.enter_email("invalid-email")

    checkout_page.enter_city("New York")
    checkout_page.enter_address("123 Test Street")
    checkout_page.enter_zip_code("10001")
    checkout_page.enter_phone("1234567890")

    checkout_page.continue_billing()

    assert checkout_page.is_validation_error_displayed(
        checkout_page.country_error
    )
@pytest.mark.validation
def test_billing_first_name_required(checkout_page):

    # First Name intentionally left EMPTY

    checkout_page.enter_last_name("Demo")
    checkout_page.enter_email("hassandemo@example.com")

    checkout_page.select_country("United States")

    checkout_page.enter_city("New York")
    checkout_page.enter_address("123 Test Street")
    checkout_page.enter_zip_code("10001")
    checkout_page.enter_phone("1234567890")

    checkout_page.continue_billing()

    assert checkout_page.is_validation_error_displayed(
        checkout_page.first_name_error
    )

@pytest.mark.validation
def test_billing_last_name_required(checkout_page):
    checkout_page.enter_first_name("Hassan")

    # Last Name intentionally left EMPTY

    checkout_page.enter_email("hassandemo@example.com")

    checkout_page.select_country("United States")

    checkout_page.enter_city("New York")
    checkout_page.enter_address("123 Test Street")
    checkout_page.enter_zip_code("10001")
    checkout_page.enter_phone("1234567890")

    checkout_page.continue_billing()

    assert checkout_page.is_validation_error_displayed(
        checkout_page.last_name_error
    )

@pytest.mark.validation
def test_billing_email_required(checkout_page):

    checkout_page.enter_first_name("Hassan")
    checkout_page.enter_last_name("Demo")

    # Email intentionally left EMPTY

    checkout_page.select_country("United States")
    checkout_page.enter_city("New York")
    checkout_page.enter_address("123 Test Street")
    checkout_page.enter_zip_code("10001")
    checkout_page.enter_phone("1234567890")

    checkout_page.continue_billing()

    assert checkout_page.is_validation_error_displayed(
        checkout_page.email_error
    )


def test_billing_invalid_email(checkout_page):

    checkout_page.enter_first_name("Hassan")
    checkout_page.enter_last_name("Demo")

    checkout_page.enter_email("invalid-email")

    checkout_page.select_country("United States")
    checkout_page.enter_city("New York")
    checkout_page.enter_address("123 Test Street")
    checkout_page.enter_zip_code("10001")
    checkout_page.enter_phone("1234567890")

    checkout_page.continue_billing()

    assert checkout_page.is_validation_error_displayed(
        checkout_page.invalid_email
    )

@pytest.mark.validation
def test_billing_city_required(checkout_page):

    checkout_page.enter_first_name("Hassan")
    checkout_page.enter_last_name("Demo")
    checkout_page.enter_email("hassandemo@example.com")

    checkout_page.select_country("United States")

    # City intentionally left EMPTY

    checkout_page.enter_address("123 Test Street")
    checkout_page.enter_zip_code("10001")
    checkout_page.enter_phone("1234567890")

    checkout_page.continue_billing()

    assert checkout_page.is_validation_error_displayed(
        checkout_page.city_error
    )

@pytest.mark.validation
def test_billing_address_required(checkout_page):

    checkout_page.enter_first_name("Hassan")
    checkout_page.enter_last_name("Demo")
    checkout_page.enter_email("hassandemo@example.com")

    checkout_page.select_country("United States")
    checkout_page.enter_city("New York")

    # Address intentionally left EMPTY

    checkout_page.enter_zip_code("10001")
    checkout_page.enter_phone("1234567890")

    checkout_page.continue_billing()

    assert checkout_page.is_validation_error_displayed(
        checkout_page.address_error
    )

@pytest.mark.validation
def test_billing_zip_required(checkout_page):

    checkout_page.enter_first_name("Hassan")
    checkout_page.enter_last_name("Demo")
    checkout_page.enter_email("hassandemo@example.com")

    checkout_page.select_country("United States")
    checkout_page.enter_city("New York")
    checkout_page.enter_address("123 Test Street")

    # ZIP intentionally left EMPTY

    checkout_page.enter_phone("1234567890")

    checkout_page.continue_billing()

    assert checkout_page.is_validation_error_displayed(
        checkout_page.zip_error
    )

@pytest.mark.validation
def test_billing_phone_required(checkout_page):

    checkout_page.enter_first_name("Hassan")
    checkout_page.enter_last_name("Demo")
    checkout_page.enter_email("hassandemo@example.com")

    checkout_page.select_country("United States")
    checkout_page.enter_city("New York")
    checkout_page.enter_address("123 Test Street")
    checkout_page.enter_zip_code("10001")

    # Phone intentionally left EMPTY

    checkout_page.continue_billing()

    assert checkout_page.is_validation_error_displayed(
        checkout_page.phone_error
    )
@pytest.mark.validation
def test_shipping_first_name_required(checkout_page):

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

    # Shipping First Name intentionally left EMPTY

    checkout_page.enter_shipping_last_name("Demo")
    checkout_page.enter_shipping_email("hassandemo@example.com")

    checkout_page.select_shipping_country("United States")
    checkout_page.enter_shipping_city("New York")
    checkout_page.enter_shipping_address("123 Test Street")
    checkout_page.enter_shipping_zip_code("10001")
    checkout_page.enter_shipping_phone("1234567890")

    checkout_page.continue_shipping_address()

    assert checkout_page.is_validation_error_displayed(
        checkout_page.shipping_first_name_error
    )
@pytest.mark.validation
def test_shipping_last_name_required(checkout_page):

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

    # Shipping Last Name intentionally left EMPTY

    checkout_page.enter_shipping_email("hassandemo@example.com")
    checkout_page.select_shipping_country("United States")
    checkout_page.enter_shipping_city("New York")
    checkout_page.enter_shipping_address("123 Test Street")
    checkout_page.enter_shipping_zip_code("10001")
    checkout_page.enter_shipping_phone("1234567890")

    checkout_page.continue_shipping_address()

    assert checkout_page.is_validation_error_displayed(
        checkout_page.shipping_last_name_error
    )

@pytest.mark.validation
def test_shipping_email_required(checkout_page):

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

    # Shipping Email intentionally left EMPTY

    checkout_page.select_shipping_country("United States")
    checkout_page.enter_shipping_city("New York")
    checkout_page.enter_shipping_address("123 Test Street")
    checkout_page.enter_shipping_zip_code("10001")
    checkout_page.enter_shipping_phone("1234567890")

    checkout_page.continue_shipping_address()

    assert checkout_page.is_validation_error_displayed(
        checkout_page.shipping_email_error
    )


def test_shipping_invalid_email(checkout_page):

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
    checkout_page.enter_shipping_email("invalid-email")

    checkout_page.select_shipping_country("United States")
    checkout_page.enter_shipping_city("New York")
    checkout_page.enter_shipping_address("123 Test Street")
    checkout_page.enter_shipping_zip_code("10001")
    checkout_page.enter_shipping_phone("1234567890")

    checkout_page.continue_shipping_address()

    # Use the actual invalid-email validation locator
    assert checkout_page.is_validation_error_displayed(
        checkout_page.shipping_email_error
    )

@pytest.mark.validation
def test_shipping_country_required(checkout_page):

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

    # Shipping Country intentionally left unselected

    checkout_page.enter_shipping_city("New York")
    checkout_page.enter_shipping_address("123 Test Street")
    checkout_page.enter_shipping_zip_code("10001")
    checkout_page.enter_shipping_phone("1234567890")

    checkout_page.continue_shipping_address()

    assert checkout_page.is_validation_error_displayed(
        checkout_page.shipping_country_error
    )

@pytest.mark.validation
def test_shipping_city_required(checkout_page):

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

    # Shipping City intentionally left EMPTY

    checkout_page.enter_shipping_address("123 Test Street")
    checkout_page.enter_shipping_zip_code("10001")
    checkout_page.enter_shipping_phone("1234567890")

    checkout_page.continue_shipping_address()

    assert checkout_page.is_validation_error_displayed(
        checkout_page.shipping_city_error
    )

@pytest.mark.validation
def test_shipping_address_required(checkout_page):

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

    # Shipping Address intentionally left EMPTY

    checkout_page.enter_shipping_zip_code("10001")
    checkout_page.enter_shipping_phone("1234567890")

    checkout_page.continue_shipping_address()

    assert checkout_page.is_validation_error_displayed(
        checkout_page.shipping_address_error
    )

@pytest.mark.validation
def test_shipping_zip_required(checkout_page):

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

    # Shipping ZIP intentionally left EMPTY

    checkout_page.enter_shipping_phone("1234567890")

    checkout_page.continue_shipping_address()

    assert checkout_page.is_validation_error_displayed(
        checkout_page.shipping_zip_error
    )

@pytest.mark.validation
def test_shipping_phone_required(checkout_page):

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

    # Shipping Phone intentionally left EMPTY

    checkout_page.continue_shipping_address()

    assert checkout_page.is_validation_error_displayed(
        checkout_page.shipping_phone_error
    )

