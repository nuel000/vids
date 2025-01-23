import logging
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
import time
import os

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def setup_driver():
    logger.info("Setting up Chrome driver...")
    options = uc.ChromeOptions()
    
    # GitHub Actions specific configurations
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-infobars')
    
    # Specify Chrome version if needed
    return uc.Chrome(version_main=131, options=options)

def login_to_google(driver, username, password):
    """Perform Google login with detailed logging and error handling"""
    try:
        logger.info("Navigating to Google login page...")
        driver.get('https://accounts.google.com/ServiceLogin')
        
        # Email input
        logger.info("Entering username...")
        email_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="email"]'))
        )
        email_input.clear()
        email_input.send_keys(username)
        
        # Next button
        logger.info("Clicking next button...")
        next_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]'))
        )
        next_button.click()
        
        # Wait for password page
        time.sleep(5)
        
        # Password input
        logger.info("Entering password...")
        password_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))
        )
        password_input.clear()
        password_input.send_keys(password)
        
        # Login button
        logger.info("Clicking login button...")
        password_next = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]'))
        )
        password_next.click()
        
        # Wait for login
        WebDriverWait(driver, 15).until(
            EC.url_contains('myaccount.google.com')
        )
        
        logger.info("Login successful!")
        return True
    
    except Exception as e:
        logger.error(f"Login failed: {e}")
        return False

def main():
    # Hardcoded credentials for testing
    username = 'momohemmanuel073'
    password = 'Ilovemymummy22@@..'
    
    driver = None
    try:
        driver = setup_driver()
        
        # Perform login
        if login_to_google(driver, username, password):
            # Navigate to desired page
            driver.get('https://myadcenter.google.com/controls?ref=my-account&ref-media=WEB&hl=en')
            
            # Optional: Take screenshot
            screenshot_dir = os.path.join(os.getcwd(), 'screenshots')
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, 'login_success.png')
            driver.save_screenshot(screenshot_path)
            logger.info(f"Screenshot saved to {screenshot_path}")
        
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        
        # Save error screenshot
        screenshot_dir = os.path.join(os.getcwd(), 'screenshots')
        os.makedirs(screenshot_dir, exist_ok=True)
        error_screenshot_path = os.path.join(screenshot_dir, 'error_screenshot.png')
        driver.save_screenshot(error_screenshot_path)
        logger.info(f"Error screenshot saved to {error_screenshot_path}")
    
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()
