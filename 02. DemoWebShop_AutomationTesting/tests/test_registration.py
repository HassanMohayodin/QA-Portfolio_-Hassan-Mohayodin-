import pytest

from pages.register_page import RegisterPage
from utils.test_data import generate_unique_email

@pytest.mark.authentication
@pytest.mark.regression

def test_successful_registration(driver):

    driver.get("https://demowebshop.tricentis.com/register")

    register_page = RegisterPage(driver)

    email = generate_unique_email()

    register_page.select_gender("male")

    assert driver.find_element(
        *register_page.gender_male
    ).is_selected()

    register_page.register(
        "Bassam",
        "Demo",
        email,
        "Pass12345"
    )

    assert register_page.is_registration_successful()

    register_page.click_continue()