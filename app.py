import sys
from playwright.sync_api import Playwright, sync_playwright
import time
from bs4 import BeautifulSoup

def flushstd(message):
    print(message)
    sys.stdout.flush()

def run(playwright: Playwright) -> None:
    try:
        browser = playwright.firefox.launch(headless=True)  # Set headless=False for debugging
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
        page = context.new_page()
        page.goto("https://accounts.google.com")
        time.sleep(random.uniform(2, 5))  # Random delay to mimic human behavior

        # Fill in email
        page.get_by_label("Email or phone").fill("momohemmanuel073")
        time.sleep(random.uniform(1, 3))
        page.get_by_label("Email or phone").press("Enter")
        time.sleep(random.uniform(2, 5))

        # Fill in password
        page.get_by_label("Enter your password").fill("Ilovemymummy22@@..")
        time.sleep(random.uniform(1, 3))
        page.get_by_label("Enter your password").press("Enter")
        flushstd('PASSSED')
        time.sleep(random.uniform(5, 10))  # Wait for login to complete

        # Navigate to the target page
        page.goto("https://myadcenter.google.com/controls?ref=my-account&ref-media=WEB&hl=en")
        time.sleep(random.uniform(5, 10))
        
        
        s= BeautifulSoup(page.content(),'html.parser')
        flushstd(s.text)
        time.sleep(3)
        

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
