import sys
from playwright.sync_api import Playwright, sync_playwright
import time
from bs4 import BeautifulSoup

def flushstd(message):
    print(message)
    sys.stdout.flush()

def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(headless=True)  # Use headless=True for CI environments
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://accounts.google.com")

    time.sleep(3)
    flushstd("Navigated to Google account login page.")
    page.get_by_label("Email or phone").fill("momohemmanuel073")
    flushstd("Email/phone field filled.")
    time.sleep(3)
    page.get_by_label("Email or phone").press("Enter")
    flushstd("Pressed Enter for email/phone field.")
    time.sleep(3)
    page.get_by_label("Enter your password").fill("Ilovemymummy22@@..")
    flushstd("Password field filled.")
    time.sleep(3)
    page.get_by_label("Enter your password").press("Enter")
    flushstd("Pressed Enter for password.")
    time.sleep(6)

    page.goto("https://myadcenter.google.com/controls?ref=my-account&ref-media=WEB&hl=en")
    flushstd("Navigated to My Ad Center page.")

    time.sleep(3)
    s = BeautifulSoup(page.content(), 'html.parser')
    google_account_info = s.find('div', class_='KT87l').text if s.find('div', class_='KT87l') else "Info not found"
    others = s.find('ul', class_='NBZP0e cIN7te xbmkib').text if s.find('ul', class_='NBZP0e cIN7te xbmkib') else "Others not found"
    flushstd(f"Google Account Info: {google_account_info}")
    flushstd(f"Others: {others}")
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
