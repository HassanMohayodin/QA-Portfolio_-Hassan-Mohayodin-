import pytest
from selenium import webdriver

from pages.home_page import HomePage
from pages.search_result_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.logger import get_logger
from utils.screenshot_helper import take_screenshot


logger = get_logger(__name__)

def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on: chrome or firefox"
    )

    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode"
    )

@pytest.fixture
def driver(request):

    browser = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")

    logger.info(
        f"Starting {browser} browser | Headless: {headless}"
    )

    if browser == "chrome":

        options = webdriver.ChromeOptions()

        if headless:
            options.add_argument("--headless=new")

        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":

        options = webdriver.FirefoxOptions()

        if headless:
            options.add_argument("--headless")

        driver = webdriver.Firefox(options=options)

    else:

        raise ValueError(
            f"Unsupported browser: {browser}. "
            "Supported browsers are: chrome and firefox."
        )

    if headless:
        driver.set_window_size(1920, 1080)
    else:
        driver.maximize_window()

    yield driver

    logger.info("Closing browser")

    driver.quit()


@pytest.fixture
def home_page(driver):

    logger.info("Opening Demo Web Shop homepage")

    driver.get("https://demowebshop.tricentis.com/")

    return HomePage(driver)


@pytest.fixture
def search_results(home_page):

    logger.info("Initializing Search Results page")

    return SearchResultsPage(home_page.driver)


@pytest.fixture
def product_page(home_page, search_results):

    logger.info("Searching for product: computer")

    home_page.search("computer")

    product_name = "Build your own cheap computer"

    logger.info(f"Opening product: {product_name}")

    search_results.open_product(product_name)

    return ProductPage(home_page.driver)


@pytest.fixture
def cart_page(product_page):

    logger.info("Adding product to cart")

    product_page.add_to_cart()

    cart_page = CartPage(product_page.driver)

    logger.info("Opening shopping cart")

    cart_page.open_cart()

    return cart_page


@pytest.fixture
def checkout_page(cart_page):

    logger.info("Agreeing to terms and conditions")

    cart_page.agree_to_terms()

    logger.info("Proceeding to checkout")

    cart_page.checkout()

    checkout_page = CheckoutPage(cart_page.driver)

    logger.info("Checking out as guest")

    checkout_page.checkout_as_guest()

    return checkout_page


@pytest.fixture(autouse=True)
def screenshot_on_failure(request, driver):

    yield

    if hasattr(request.node, "rep_call"):

        if request.node.rep_call.failed:

            test_name = request.node.name

            screenshot_path = take_screenshot(
                driver,
                test_name
            )

            logger.error(
                f"Test failed: {test_name}. "
                f"Screenshot saved at: {screenshot_path}"
            )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call":

        item.rep_call = report