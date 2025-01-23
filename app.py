from playwright.sync_api import Playwright, sync_playwright, expect
import time
from bs4 import BeautifulSoup
import sys
from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import os

def flushstd(message):
    print(message)
    sys.stdout.flush()



def run(playwright) -> None:
    # Launch the browser in non-headless mode (Xvfb will handle the display)
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    try:
        # Navigate to Google login page
        page.goto("https://accounts.google.com")
        print("Navigated to Google login page")
        time.sleep(3)

        # Fill in the email
        page.get_by_label("Email or phone").fill("momohemmanuel073")
        flushstd("Emailed Filled")
        time.sleep(3)

        # Click the "Next" button
        page.get_by_label("Email or phone").press("Enter")
        flushstd("NEXT Filled")
        time.sleep(3)

        # Fill in the password
        s = BeautifulSoup(page.content(), 'html.parser')
        flushstd(s.text)
        page.get_by_label("Enter your password").fill("Ilovemymummy22@@..")
        flushstd("PAASSS Filled")
        time.sleep(3)

        # Click the "Next" button
        page.get_by_label("Enter your password").press("Enter")
        print("Password next button clicked")
        time.sleep(6)

        # Navigate to the target page
        page.goto("https://myadcenter.google.com/controls?ref=my-account&ref-media=WEB&hl=en")
        print("Navigated to myadcenter.google.com")
        time.sleep(3)

        # Parse the page content
        s = BeautifulSoup(page.content(), 'html.parser')
        google_account_info = s.find('div', class_='KT87l').text
        others = s.find('ul', class_='NBZP0e cIN7te xbmkib').text
        print("Google Account Info:", google_account_info)
        print("Other Info:", others)

        # Take a screenshot (optional)
        screenshot_dir = os.path.join(os.getcwd(), 'screenshots')
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, 'page_screenshot.png')
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        context.close()
        browser.close()
        print("Browser closed")

with sync_playwright() as playwright:
    run(playwright)
