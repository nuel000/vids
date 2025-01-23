import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

username = 'momohemmanuel073'
password = 'Ilovemymummy22@@..'

# Options for headless mode and stealth

options = uc.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--disable-gpu')  # Disable GPU acceleration
options.add_argument('--no-sandbox')  # Bypass OS security model

# Pass the exact ChromeDriver version
driver = uc.Chrome(version_main=114, options=options)


try:
    # Clear all cookies
    driver.delete_all_cookies()

    # Navigate to login page
    driver.get('https://accounts.google.com/ServiceLogin')

    # Wait for email input and enter username
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="email"]'))
    )
    email_input.clear()
    email_input.send_keys(username)

    # Click next button
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]'))
    )
    next_button.click()
    sleep(10)

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))
    )
    password_input.clear()
    password_input.send_keys(password)

    # Click password next button
    password_next = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]'))
    )
    password_next.click()

    # Wait and navigate to Gmail
    WebDriverWait(driver, 10).until(
        EC.url_contains('myaccount.google.com')
    )
    driver.get('https://myadcenter.google.com/controls?ref=my-account&ref-media=WEB&hl=en')

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Always close the browser
    driver.quit()
