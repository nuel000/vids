import sys
import random
from playwright.sync_api import Playwright, sync_playwright
import time
from bs4 import BeautifulSoup

def flushstd(message):
    print(message)
    sys.stdout.flush()



from playwright.sync_api import Playwright, sync_playwright, expect
import time
from bs4 import BeautifulSoup

def run(playwright: Playwright) -> None:
    # Proxy configuration
    proxy = {
        "server": "geo.iproyal.com:12321",
        "username": "wqNuPj2DGRxc2DzQ",
        "password": "TJ9Iy9u5iEhg4Axe"
    }

    browser = playwright.firefox.launch(
        headless=True,
        proxy=proxy,
        args=[
            '--disable-blink-features=AutomationControlled',
            '--no-sandbox',
            '--disable-setuid-sandbox',
            '--disable-infobars',
            '--window-position=0,0',
            '--ignore-certifcate-errors',
            '--ignore-certifcate-errors-spki-list',
        ]
    )
    
    # Enhanced context settings
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
        locale='en-US',
        timezone_id='America/New_York',
        permissions=['geolocation'],
        java_script_enabled=True,
    )

    context.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
    """)
    
    page = context.new_page()
    
    def random_sleep(min_time=2, max_time=4):
        time.sleep(min_time + (max_time - min_time) * 0.5)
    
    try:
        # First verify proxy is working
        page.goto("https://ipinfo.io", wait_until="networkidle")
        flushstd("Current IP info:", page.content())
        random_sleep()
        
        page.goto("https://accounts.google.com", wait_until="networkidle")
        random_sleep()
        
        email_input = page.get_by_label("Email or phone")
        email_input.click()
        email_input.type("momohemmanuel073", delay=100)
        random_sleep()
        email_input.press("Enter")
        random_sleep()
        
        password_input = page.get_by_label("Enter your password")
        password_input.click()
        password_input.type("Ilovemymummy22@@..", delay=100)
        random_sleep()
        password_input.press("Enter")
        random_sleep(5, 7)
        
        page.goto("https://myadcenter.google.com/controls?ref=my-account&ref-media=WEB&hl=en", 
                 wait_until="networkidle")
        random_sleep()
        
        s = BeautifulSoup(page.content(), 'html.parser')
        google_account_info = s.find('div', class_='KT87l').text
        others = s.find('ul', class_='NBZP0e cIN7te xbmkib').text
        
        print(google_account_info)
        print(others)
        
        random_sleep(5, 7)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        page.screenshot(path="error_screenshot.png")
    finally:
        context.close()
        browser.close()

with sync_playwright() as playwright:
    run(playwright)
