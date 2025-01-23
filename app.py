import undetected_chromedriver as uc
import chromedriver_autoinstaller
import time
import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def flushstd(message):
    print(message)
    sys.stdout.flush()

def take_screenshot(driver, filename):
    """Take a screenshot and save it to the specified filename."""
    screenshot_dir = os.path.join(os.getcwd(), 'screenshots')
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_path = os.path.join(screenshot_dir, filename)
    driver.save_screenshot(screenshot_path)
    flushstd(f"Screenshot saved: {screenshot_path}")

username = 'momohemmanuel073'
password = 'Ilovemymummy22@@..'

# Automatically install the correct version of ChromeDriver
chromedriver_autoinstaller.install()

# Set up Chrome options
options = uc.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--disable-gpu')  # Disable GPU acceleration
options.add_argument('--no-sandbox')  # Bypass OS security model, required for cloud environments
options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-infobars')

# Launch the browser
driver = uc.Chrome(options=options)
time.sleep(5)

try:
    # Clear all cookies
    driver.delete_all_cookies()

    # Navigate to login page
    driver.get('https://accounts.google.com/ServiceLogin')
    flushstd('Navigated to Google login page')
    sleep(3)  # Add delay to mimic human behavior

    # Wait for email input and enter username
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="email"]'))
    )
    email_input.clear()
    email_input.send_keys(username)
    flushstd('Username entered')
    sleep(2)  # Add delay to mimic human behavior

    # Click next button
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]'))
    )
    next_button.click()
    flushstd('Next button clicked')
    sleep(5)  # Add delay to mimic human behavior

    # Take a screenshot after clicking the "Next" button
    take_screenshot(driver, 'after_next_button_click.png')

    # Wait for password input and enter password
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))
    )
    password_input.clear()
    password_input.send_keys(password)
    flushstd('Password entered')
    sleep(2)  # Add delay to mimic human behavior

    # Click password next button
    password_next = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]'))
    )
    password_next.click()
    flushstd('Password next button clicked')
    sleep(5)  # Add delay to mimic human behavior

    # Wait and navigate to Gmail
    WebDriverWait(driver, 10).until(
        EC.url_contains('myaccount.google.com')
    )
    flushstd('Login successful, navigating to myadcenter.google.com')
    sleep(3)  # Add delay to mimic human behavior

    # Navigate to the target page
    driver.get('https://myadcenter.google.com/controls?ref=my-account&ref-media=WEB&hl=en')
    flushstd('Navigated to myadcenter.google.com')
    sleep(5)  # Add delay to mimic human behavior

except Exception as e:
    print(f"An error occurred: {e}")
    # Take a screenshot if an error occurs
    take_screenshot(driver, 'error_screenshot.png')

finally:
    # Always close the browser
    driver.quit()
    flushstd('Browser closed')
