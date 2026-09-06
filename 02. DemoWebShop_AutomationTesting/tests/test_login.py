import pytest
from pages.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.authentication
@pytest.mark.parametrize("email,password", [
    ("wrong@email.com", "WrongPassword123"),
    ("HassanDemo@example.com", "WrongPassword123"),
    ("", "Password123"),
    ("HassanDemo@example.com", ""),
])
def test_invalid_login(driver, email, password):

    driver.get("https://demowebshop.tricentis.com/login")

    login_page = LoginPage(driver)

    login_page.login(
        email,
        password
    )

    assert login_page.is_login_error_displayed()

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.authentication
def test_valid_login(driver):

    driver.get("https://demowebshop.tricentis.com/login")

    login_page = LoginPage(driver)

    login_page.login(
        "HassanDemo@example.com",
        "Password123"
    )

    assert login_page.is_logged_in()