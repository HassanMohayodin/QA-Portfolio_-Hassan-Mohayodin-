Demo Web Shop Automation Testing Framework
Project Overview

This project is an end-to-end UI automation testing framework developed for the Demo Web Shop application.

The framework uses Python, Selenium WebDriver, and Pytest and follows the Page Object Model (POM) design pattern to maintain clean, reusable, and scalable automation code.

The automated test suite covers major e-commerce workflows, including authentication, product search, product interaction, shopping cart functionality, checkout, form validation, payment, and order confirmation.

Technologies Used
Python
Selenium WebDriver
Pytest
Pytest HTML
Pytest-xdist
Git
GitHub
Chrome WebDriver
Framework Design

The framework follows the Page Object Model (POM) architecture.

02. DemoWebShop_AutomationTesting/
│
├── config/
│   └── __init__.py
│
├── pages/
│   ├── home_page.py
│   ├── login_page.py
│   ├── register_page.py
│   ├── search_result_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests/
│   ├── test_home.py
│   ├── test_login.py
│   ├── test_registration.py
│   ├── test_search.py
│   ├── test_product.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_checkoutvalidation.py
│
├── utils/
│   ├── logger.py
│   ├── screenshot_helper.py
│   └── test_data.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
Test Coverage

The automation suite covers the following areas:

Module	Coverage
Home Page	Homepage loading and accessibility
Login	Valid and invalid login scenarios
Registration	Successful user registration
Search	Product search and no-result scenarios
Product	Product page interaction and add-to-cart
Cart	Product validation, quantity update, removal, and checkout
Billing	Required field validation
Shipping Address	Required field and invalid email validation
Shipping Method	Ground, next-day, and second-day shipping
Payment Method	Cash on Delivery
Payment Information	Payment information confirmation
Order Confirmation	Successful order placement and continuation
Total Automated Tests

43 automated test cases

Key Features
Page Object Model

Each major application page is represented by a dedicated Page Object class.

This improves:

Code reusability
Test maintainability
Separation between test logic and UI locators
Framework scalability
Pytest Fixtures

Fixtures are managed through conftest.py.

The framework automatically handles:

Browser initialization
Browser termination
Homepage navigation
Product setup
Cart setup
Checkout setup
Test Markers

Tests are organized using Pytest markers.

Available markers include:

smoke
regression
authentication
cart
checkout
validation

Example:

pytest -m smoke

Run authentication tests:

pytest -m authentication

Run validation tests:

pytest -m validation
Logging

The framework includes centralized logging.

Logs capture important automation events such as:

Browser startup
Homepage navigation
Product searching
Product selection
Cart operations
Checkout operations
Browser shutdown

Logs help with debugging and execution analysis.

Screenshot on Failure

The framework automatically captures screenshots when a test fails.

Screenshots are saved with:

Test name
Execution timestamp

Example:

screenshots/
└── test_order_success_continue_2026-09-05_19-04-19.png
Parallel Test Execution

The framework supports parallel test execution using pytest-xdist.

Example:

pytest -n 2

This runs tests across two parallel workers.

HTML Test Reports

HTML reports can be generated using pytest-html.

Example:

pytest --html=reports/report.html --self-contained-html

The generated report contains:

Test execution results
Passed tests
Failed tests
Execution duration
Environment information
Installation
Clone the Repository
git clone https://github.com/HassanMohayodin/QA-Engineer-Portfolio.git

Navigate to:

cd "QA-Engineer-Portfolio/02. DemoWebShop_AutomationTesting"
Install Dependencies
pip install -r requirements.txt
Running Tests

Run the complete test suite:

pytest

Run a specific test file:

pytest tests/test_login.py

Run tests with verbose output:

pytest -v

Run smoke tests:

pytest -m smoke

Run regression tests:

pytest -m regression

Run tests in parallel:

pytest -n 2
Application Under Test

The automation framework tests:

Demo Web Shop

https://demowebshop.tricentis.com/

Demo Web Shop is an e-commerce application used for practicing software testing and automation testing concepts.

Author

Hassan Mohayodin

Aspiring Software Quality Assurance Engineer focused on:

Manual Testing
Automation Testing
Selenium
Python
API Testing
SQL
Software Quality Assurance
