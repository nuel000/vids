import sys
from playwright.sync_api import Playwright, sync_playwright
import time
from bs4 import BeautifulSoup

def flushstd(message):
    print(message)
    sys.stdout.flush()

def run(playwright: Playwright) -> None:
    try:


        browser = playwright.chromium.launch(
        headless=True,  # Set headless to True if you don't want a visible browser
        args=[
            '--disable-blink-features=AutomationControlled',
            '--no-sandbox',  # May help in some environments
            '--disable-web-security',  # Not recommended for production use
            '--disable-infobars',  # Prevent infobars
            '--disable-extensions',  # Disable extensions
            '--start-maximized',  # Start maximized
            '--window-size=1280,720'  # Set a specific window size
        ]
        )  # Use headless=True for headless mode
        context = browser.new_context()

        page = context.new_page()

        page.goto("https://stackoverflow.com/")
        with page.expect_popup() as page1_info:
            page.frame_locator("iframe[title=\"Sign in with Google Dialogue\"]").get_by_role("button", name="Continue").click()

        time.sleep(3)
        page1 = page1_info.value

        time.sleep(3)
        page1.close()

        
        s= BeautifulSoup(page.content(),'html.parser')
        flushstd(s.text)
        time.sleep(3)
        


        time.sleep(3)
        # page.get_by_role("menuitem", name="Log in").click()
        # time.sleep(3)
        # page.get_by_role("button", name="Log in with Google").click()
        # time.sleep(3)

        # flushstd('password filled')
        # time.sleep(3)
        # page.get_by_role("button", name="Next").click()
        # flushstd('Next Pressed')
        # time.sleep(3)
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
