import pytest


@pytest.mark.regression
def test_open_product(product_page):

    product_name = "Build your own cheap computer"

    assert product_page.get_product_title() == product_name

@pytest.mark.regression
def test_add_product_to_cart(product_page):

    product_name = "Build your own cheap computer"

    assert product_page.get_product_title() == product_name

    product_page.add_to_cart()

    assert product_page.is_product_added_to_cart()