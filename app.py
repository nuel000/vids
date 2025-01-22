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

        page.goto("https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")
        time.sleep(3)
        page.get_by_role("button", name="Log in with Google").click()
        time.sleep(3)
        page.goto("https://accounts.google.com/v3/signin/identifier?opparams=%253F&dsh=S-416685054%3A1737569744090319&client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&ddm=1&o2v=1&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&response_type=code&scope=profile+email&service=lso&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3A1b8%2C16%3A1fae7a5d566b956d%2C10%3A1737569743%2C16%3Ace5233fcf656064b%2C60d483648b30f7692962d4fc4f690dc9bc8f651e9b4dbc9a1d30471ddeedab26%22%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%2256c23cfc664341e59db72b7ff778770a%22%7D&flowName=GeneralOAuthFlow&continue=https%3A%2F%2Faccounts.google.com%2Fsignin%2Foauth%2Fconsent%3Fauthuser%3Dunknown%26part%3DAJi8hANKe4FUH-0G7bVy6UP99fVD71h2--k2O3gJ54VFShMrd0OyJn2jh4gpn3N9OdeXCaHddrJl_bZNKSSJ09eOV0HSP8XTfOLT1lJK72V__AqU8MbaviiGkRsfiZkD3PH2RaLQuhvrd4QdXT24T8E3lKD6E_8O1iAHwqIh4KBoAusLxQGS8uTZZ8qaUchw7Q1i92VbWyBVdRaQYnRi-LmLlDAJXAERvPVyXlAiqAY1ORNS4DJVcsvWgcLHArS6Fwab83_lJBWGQR_Q59ebM-yx35yQ5SLxKuAMA4Orw-5dtHLGsziOoFVxZTgu8Yyb0AaeNT9AfpIjVeKI2i_sHIqqnAJUj8A6o15F1yjroPKcTFk-aeHA1Xg4gqyNbwp8l83MrV79V0nqPYdaG5c1kq9OMBjYr7eGO879X_sicPXNRXEH9_Dq6L8XQa6YmDeNTGwjgFj4rImPcKzi0_jUJ4kuU4V-iS8mKA%26flowName%3DGeneralOAuthFlow%26as%3DS-416685054%253A1737569744090319%26client_id%3D717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%23&app_domain=https%3A%2F%2Fstackauth.com&rart=ANgoxcdqFRKuGVsFMtkPnApJSgDrvnpZBV5j6JdRgFMn_ieB3PZ5FQw9gn2_kM105og_oZ-kkY1ttEGgQAwfasgZlM8xyhrLeDn2WwHDJCGDmjajqVekESA")
        time.sleep(3)
        page.get_by_label("Email or phone").click()
        page.get_by_label("Email or phone").fill("momohemmanuel073")
        flushstd('eMAIL FILLED')
        time.sleep(3)
        page.get_by_role("button", name="Next").click()
        time.sleep(3)
        page.get_by_label("Enter your password").click()
        page.get_by_label("Enter your password").fill("Ilovemymummy22@@..")
        flushstd('pass FILLED')
        time.sleep(3)
        page.get_by_role("button", name="Next").click()
        page.goto("https://stackoverflow.com/")
        
        time.sleep(3)
        page.goto("https://stackoverflow.com/")

        time.sleep(3)
        # page.get_by_role("menuitem", name="Log in").click()
        # time.sleep(3)
        # page.get_by_role("button", name="Log in with Google").click()
        # time.sleep(3)
        # page.get_by_label("Email or phone").click()
        # time.sleep(3)
        # page.get_by_label("Email or phone").fill("momohemmanuel073")
        # time.sleep(3)
        # page.get_by_label("Email or phone").press("Enter")
        # flushstd('Mail Enter Pressed')
        # time.sleep(3)
        # page.get_by_label("Enter your password").click()
        # time.sleep(3)
        # page.get_by_label("Enter your password").fill("Ilovemymummy22@@..")
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
