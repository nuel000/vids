import sys
from playwright.sync_api import Playwright, sync_playwright
import time
from bs4 import BeautifulSoup

def flushstd(message):
    print(message)
    sys.stdout.flush()

def run(playwright: Playwright) -> None:
    try:

        # Launch Chrome browser with options
        browser = playwright.firefox.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://stackoverflow.com/")
        page.frame_locator("iframe[title=\"Sign in with Google Dialogue\"]").get_by_label("Close").click()
        time.sleep(3)
        page.get_by_role("menuitem", name="Log in").click()
        time.sleep(3)
        page.get_by_role("button", name="Log in with Google").click()
        time.sleep(3)
        page.get_by_label("Email or phone").click()
        time.sleep(3)
        page.get_by_label("Email or phone").fill("momohemmanuel073")
        time.sleep(3)
        page.get_by_label("Email or phone").press("Enter")
        flushstd('Mail Enter Pressed')
        time.sleep(3)
        page.get_by_label("Enter your password").click()
        time.sleep(3)
        page.get_by_label("Enter your password").fill("Ilovemymummy22@@..")
        flushstd('password filled')
        time.sleep(3)
        page.get_by_role("button", name="Next").click()
        flushstd('Next Pressed')
        time.sleep(3)
        # Take screenshot
        screenshot_path = "screenshot.png"
        page.screenshot(path=screenshot_path)
        flushstd(f"Screenshot taken and saved as {screenshot_path}")
        # Navigate to Ad Center
        page.goto("https://myadcenter.google.com/controls?ref=my-account&ref-media=WEB&hl=en")

        flushstd("Navigated to My Ad Center page.")
        time.sleep(3)

        # Parse content
        s = BeautifulSoup(page.content(), 'html.parser')
        google_account_info = s.find('div', class_='KT87l').text if s.find('div', class_='KT87l') else "Info not found"
        others = s.find('ul', class_='NBZP0e cIN7te xbmkib').text if s.find('ul', class_='NBZP0e cIN7te xbmkib') else "Others not found"

        flushstd(f"Google Account Info: {google_account_info}")
        flushstd(f"Others: {others}")

    except Exception as e:
        flushstd(f"An error occurred: {str(e)}")
        # Take error screenshot if possible
        try:
            page.screenshot(path="error_screenshot.png")
        except:
            pass
    finally:
        context.close()
        browser.close()

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
