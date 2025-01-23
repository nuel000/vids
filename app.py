import undetected_chromedriver.v2 as uc
import chromedriver_autoinstaller

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

# Your scraping code here
