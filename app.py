from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def run():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--start-maximized")

    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to Google login
        driver.get("https://accounts.google.com")
        time.sleep(3)

        # Fill in email/username
        email_field = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        email_field.send_keys("momohemmanuel073")
        email_field.send_keys(Keys.ENTER)
        time.sleep(3)

        # Fill in password
        password_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        password_field.send_keys("Ilovemymummy22@@..")
        password_field.send_keys(Keys.ENTER)
        time.sleep(6)

        # Navigate to Google Ad Center page
        driver.get("https://myadcenter.google.com/controls?ref=my-account&ref-media=WEB&hl=en")
        time.sleep(3)

        # Extract content using BeautifulSoup
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        google_account_info = soup.find('div', class_='KT87l')
        others = soup.find('ul', class_='NBZP0e cIN7te xbmkib')

        # Print extracted content
        print(google_account_info.text if google_account_info else "No account info found")
        print(others.text if others else "No other info found")

        # Wait before closing
        time.sleep(60)

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    run()
