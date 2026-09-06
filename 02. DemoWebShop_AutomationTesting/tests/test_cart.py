import pytest

from pages.checkout_page import CheckoutPage
pytestmark = pytest.mark.cart


@pytest.mark.regression
def test_product_in_cart(cart_page):

    product_name = "Build your own cheap computer"

    assert cart_page.get_product_name() == product_name
    assert cart_page.get_quantity() == "1"
    assert cart_page.get_unit_price() == "815.00"
    assert cart_page.get_total_price() == "815.00"


@pytest.mark.regression
def test_update_cart_quantity(cart_page):

    cart_page.set_quantity(2)
    cart_page.update_cart()

    assert cart_page.get_quantity() == "2"
    assert cart_page.get_total_price() == "1630.00"


@pytest.mark.regression
def test_remove_product_from_cart(cart_page):

    cart_page.remove_product()
    cart_page.update_cart()

    assert cart_page.is_cart_empty()


@pytest.mark.regression
def test_proceed_to_checkout(cart_page):

    cart_page.agree_to_terms()
    cart_page.checkout()

    checkout_page = CheckoutPage(cart_page.driver)

    checkout_page.checkout_as_guest()

    assert checkout_page.is_checkout_page_displayed()