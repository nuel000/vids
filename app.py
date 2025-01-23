import undetected_chromedriver as uc
import chromedriver_autoinstaller
import time
import sys

def flushstd(message):
    print(message)
    sys.stdout.flush()


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

    # Wait for email input and enter username
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="email"]'))
    )
    email_input.clear()
    email_input.send_keys(username)
    flushstd('Username entered')



    # Click next button
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]'))

    )
    next_button.click()
    flushstd('NEXT BUTTON CLICKED')
    sleep(10)


    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))
    )
    password_input.clear()
    password_input.send_keys(password)
    flushstd('PAASSS ENTERED')

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


# Your scraping code here
