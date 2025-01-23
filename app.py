import time
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By

# Set up Chrome options
options = uc.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode (no UI)
options.add_argument('--disable-gpu')  # Disable GPU acceleration
options.add_argument('--no-sandbox')  # Required for running in Docker or restricted environments
options.add_argument('--disable-dev-shm-usage')  # Overcome resource issues in Docker
options.add_argument('--disable-blink-features=AutomationControlled')  # Bypass automation detection

# Initialize undetected chromedriver with the given options
driver = uc.Chrome(options=options)

# Example of opening a website and interacting with it
driver.get("https://www.example.com")

# Example interaction: Wait for an element and click it (adjust to your target website)
try:
    element = driver.find_element(By.ID, "some-id")
    element.click()
    print("Element clicked!")
except Exception as e:
    print(f"Error: {e}")

# You can perform more actions here, like scraping data, filling out forms, etc.

# Keep the browser running for a while to simulate interaction (optional)
time.sleep(5)

# Close the driver
driver.quit()
