import undetected_chromedriver as uc
import chromedriver_autoinstaller
import time

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
driver.get('https://accounts.google.com/ServiceLogin')
flushstd('Gotten to page')

# Your scraping code here
