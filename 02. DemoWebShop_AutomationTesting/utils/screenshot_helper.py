import os
from datetime import datetime


def take_screenshot(driver, test_name):

    screenshots_folder = "screenshots"

    os.makedirs(screenshots_folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    screenshot_name = (
        f"{test_name}_{timestamp}.png"
    )

    screenshot_path = os.path.join(
        screenshots_folder,
        screenshot_name
    )

    driver.save_screenshot(screenshot_path)

    return screenshot_path