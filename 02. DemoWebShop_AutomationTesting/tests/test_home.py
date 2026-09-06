import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.core import driver

@pytest.mark.smoke
@pytest.mark.regression
def test_demowebshop(driver):
    driver.get("https://demowebshop.tricentis.com/")

    assert "Demo Web Shop" in driver.title