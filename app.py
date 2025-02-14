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

def run(playwright: Playwright) -> None:
    try:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://adstransparency.google.com/advertiser/AR09368349516924715009?region=anywhere")
        time.sleep(10)
        flushstd('Sleeping for 10...')
        
        # Take a screenshot (optional)
        screenshot_dir = os.path.join(os.getcwd(), 'screenshots')
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, 'page_screenshot.png')
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
                # Take a screenshot (optional)
        screenshot_dir = os.path.join(os.getcwd(), 'screenshots')
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, 'page_screenshot.png')
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")

    finally:
        # Close the browser
        context.close()
        browser.close()
        print("Browser closed")

with sync_playwright() as playwright:
    run(playwright)
