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
        page.goto("https://www.google.com/search?q=google+ads+center&sca_esv=715c4e507116a0ae&source=hp&ei=HtSQZ-TQFNz5kdUPioHrgAE&iflsig=AL9hbdgAAAAAZ5DiLgNvoJyl0l1zFazQ8kMGajD_FA5Z&ved=0ahUKEwjk16_FmomLAxXcfKQEHYrAGhAQ4dUDCA4&uact=5&oq=google+ads+center&gs_lp=Egdnd3Mtd2l6IhFnb29nbGUgYWRzIGNlbnRlcjIFEAAYgAQyBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB5IjDhQyRFY4jFwAXgAkAEAmAH-AaABqxmqAQYwLjEzLjS4AQPIAQD4AQGYAhKgAvQaqAIKwgIKEAAYAxjqAhiPAcICChAuGAMY6gIYjwHCAgsQABiABBixAxiDAcICERAuGIAEGLEDGNEDGIMBGMcBwgILEC4YgAQYsQMYgwHCAg4QABiABBixAxiDARiKBcICCBAAGIAEGLEDwgIOEC4YgAQYsQMY0QMYxwHCAhEQLhiABBixAxjRAxjHARiKBZgDGPEF7pn0mLaUFAGSBwUxLjkuOKAH3nQ&sclient=gws-wiz&sei=TdSQZ_CrDOX4kdUP692dmQ4")
        time.sleep(3)
        page.goto("https://accounts.google.com")
        
        # Fill email
        page.get_by_label("Email or phone").fill("momohemmanuel073")
        time.sleep(3)
        page.get_by_label("Email or phone").press("Enter")
        flushstd("EmailFilled")
        time.sleep(3)
        page.get_by_label("Enter your password").fill("Ilovemymummy22@@..")
        flushstd("passFilled")
        time.sleep(3)
        page.get_by_label("Enter your password").press("Enter")
        time.sleep(6)
        
        # Take screenshot
        screenshot_path = "screenshot.png"
        page.screenshot(path=screenshot_path)
        flushstd(f"Screenshot taken and saved as {screenshot_path}")
        

        
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
