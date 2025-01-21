import sys
from playwright.sync_api import Playwright, sync_playwright
import time
from bs4 import BeautifulSoup

def flushstd(message):
    print(message)
    sys.stdout.flush()

def run(playwright: Playwright) -> None:
    try:
        browser = playwright.firefox.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        
        # Navigate to Google login
        page.goto("https://accounts.google.com")
        
        # Fill email
        email_input = page.get_by_label("Email or phone")
        email_input.fill("momohemmanuel073")
        flushstd("EmailFilled")
        time.sleep(3)
        
        email_input.press("Enter")
        time.sleep(6)
        flushstd("Enter Pressed")
        
        # Take screenshot
        screenshot_path = "screenshot.png"
        page.screenshot(path=screenshot_path)
        flushstd(f"Screenshot taken and saved as {screenshot_path}")
        
        flushstd("Pssword filled")
        time.sleep(3)
        
        page.get_by_label("Enter your password").press("Enter")
        flushstd("Emted pressed")
        time.sleep(6)
        
        # Navigate to Ad Center
        page.goto("https://myadcenter.google.com/controls?ref=my-account&ref-media=WEB&hl=en")
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
