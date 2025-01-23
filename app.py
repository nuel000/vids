from playwright.sync_api import Playwright, sync_playwright, expect
import time
from bs4 import BeautifulSoup
import sys

def flushstd(message):
    print(message)
    sys.stdout.flush()

def run(playwright: Playwright) -> None:

    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://accounts.google.com")

    time.sleep(3)
    page.get_by_label("Email or phone").fill("momohemmanuel073")
    time.sleep(3)
    page.get_by_label("Email or phone").press("Enter")
    flushstd('Email Filled')
    time.sleep(3)
    page.get_by_label("Enter your password").fill("Ilovemymummy22@@..")
    time.sleep(3)
    flushstd('pass Filled')
    page.get_by_label("Enter your password").press("Enter")
    time.sleep(6)

    page.goto("https://myadcenter.google.com/controls?ref=my-account&ref-media=WEB&hl=en")

    time.sleep(3)
    s =  BeautifulSoup(page.content(),'html.parser')
    google_account_info = s.find('div',class_='KT87l').text
    others = s.find('ul',class_='NBZP0e cIN7te xbmkib').text
    print(google_account_info)
    print(others)
    time.sleep(60)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
