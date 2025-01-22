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
        page.goto("https://accounts.google.com/v3/signin/identifier?opparams=%253F&dsh=S188323732%3A1737569080257578&client_id=717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com&ddm=1&o2v=1&redirect_uri=https%3A%2F%2Fstackauth.com%2Fauth%2Foauth2%2Fgoogle&response_type=code&scope=profile+email&service=lso&state=%7B%22sid%22%3A1%2C%22st%22%3A%2259%3A3%3A1b8%2C16%3A8de8b1b77e540eeb%2C10%3A1737569079%2C16%3A537a0674580d770e%2C5253f8fc05ffa68cf9e435f677d91890e1693bcf026152b6058680c98258042d%22%2C%22cid%22%3A%22717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%22%2C%22k%22%3A%22Google%22%2C%22ses%22%3A%224f66e8736f7d4758886890826731df16%22%7D&flowName=GeneralOAuthFlow&continue=https%3A%2F%2Faccounts.google.com%2Fsignin%2Foauth%2Fconsent%3Fauthuser%3Dunknown%26part%3DAJi8hAO2ei39ko2laBAgW1EfRvaOD7-moclTv7IzYrGHm7zFj3UK39o0JNJud2_8f5MgIN4C7agmvFtpYcPdYFNEQd8zy11V9EuWJUG2dh1_nklq88QuwuMvwej0bRibICoWMX6qUKCqICzSs26HOLk_1t_YOaoncpx8Hkr0rtPBpUuMWW3_eIKqErV7wimZl-M5UwSId8oQH-G274Wjg5qC0vNd2YpBp9hU-60oB6SbBuXqwohVPaJ0tEAcCWgQh_WmNLHmf9RQx6baHQpwDBf8L7GHLMjaPQpUM2TQbDphq2Cc5DL3SArruiup9T6VYNKCTsF1jjygZiMSZwD5K3hY_t4dtSoYTlo3ipYiibD6-PrlbYOCmIyVMA4JJkx87CNi5sC_C48skB25tlzrNgXzAsufg-QeiNOuFFmDvJWSWmisQ-5v4hydjAzeTjERsZ8s1BVOu3XtCKXk_RkV3fGvTmU2LAgqMw%26flowName%3DGeneralOAuthFlow%26as%3DS188323732%253A1737569080257578%26client_id%3D717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%23&app_domain=https%3A%2F%2Fstackauth.com&rart=ANgoxcflTj5IcT1gY_3edqZOH5vYCKus6W8QujO6PSp7c1xN2sFfgElUgtc2FqqfaR1prCFw6fYKzBOimrKie2uebjf8sWLOZVeaAhHaqJy1XlRI9jpF_gY")
        page.get_by_label("Email or phone").click()
        page.get_by_label("Email or phone").fill("momohemmanuel073")
        flushstd('eMAIL FILLED')
        time.sleep(3)
        page.get_by_role("button", name="Next").click()
        time.sleep(3)
        page.get_by_label("Enter your password").click()
        time.sleep(3)
        page.get_by_label("Enter your password").fill("Ilovemymummy22@@..")
        flushstd('pass FILLED')
        page.goto("https://accounts.google.com.ng/accounts/SetSID?ssdc=1&sidt=ALWU2csee01vO6RHmem7uzYXcJLnSQaFv%2BIshFPTv1NZtbpmvvrUdbQTWxtPMAcewob3VaD7iA/BjQFUH9swME6Cz10dUQXVyabQ5aCUZZjYtpOk2GDDhVZReXnSc3iKE3U2gIpMhAs1N6X2yvWy%2BbHwhMRMWbzW%2Bm8eyZhpuJjxl3A5oqqJxgVlFqldmUcJEa6NgsS8NfUXCf8TX3Tj5Ew/tqsYhJcZbc2qDgK1atW3CmJFc34Recr/C3uDoNMX%2BDgdyZ52XsvuVRzXDwO2xLROc8ehSywbGJ8FiQ2KHF9eNQn9bJPs4lYmdbHz2Gvh7svfV5Ajan6/Zn0wK6mdXtib74b1d6jLKYRp/6tPTcbOwuUmHD2eeY2DlhQ6AfELQ8JMfz%2BLCM%2Bfvux6dXDh9n0/HF4ZbkKG%2B3T2dv2ISL8654GWY2nSY7WSkMh1lq2/tyjeuDjKCG7lm/NyJxrWRxOVmvRK%2ByBLBnNRJyRObs0i9kUsE/q1QXSLtattrBfGsGZOwRfuIoVMK/LGOp542uucEhNMSGZQ2mJ4pq/Tz40eY3EbYa6HRRUuooY9nLnrMlpZdzvs1T3h3KZHLMphoR/E9AbD0ctFuycOKzURFI6n/7R1C%2B3it8G%2B1HPZsXbKD3qq7zqhKe/lfCrqhdeEfSDmWiuyjpOU6wb2le7UW4NEnR0mcvn8s4CwLGhTCRTxnOaChhE6JHtwAdzkTdsAcQqN/1dp0juGyyaEOxheujeEehlMGycvzGNP9hfhuAIkMreHgq05l3ieZO6eQYU8MXQ4gOviGTvAuA%3D%3D&continue=https://accounts.google.com/signin/oauth/consent?authuser%3D0%26part%3DAJi8hAO2ei39ko2laBAgW1EfRvaOD7-moclTv7IzYrGHm7zFj3UK39o0JNJud2_8f5MgIN4C7agmvFtpYcPdYFNEQd8zy11V9EuWJUG2dh1_nklq88QuwuMvwej0bRibICoWMX6qUKCqICzSs26HOLk_1t_YOaoncpx8Hkr0rtPBpUuMWW3_eIKqErV7wimZl-M5UwSId8oQH-G274Wjg5qC0vNd2YpBp9hU-60oB6SbBuXqwohVPaJ0tEAcCWgQh_WmNLHmf9RQx6baHQpwDBf8L7GHLMjaPQpUM2TQbDphq2Cc5DL3SArruiup9T6VYNKCTsF1jjygZiMSZwD5K3hY_t4dtSoYTlo3ipYiibD6-PrlbYOCmIyVMA4JJkx87CNi5sC_C48skB25tlzrNgXzAsufg-QeiNOuFFmDvJWSWmisQ-5v4hydjAzeTjERsZ8s1BVOu3XtCKXk_RkV3fGvTmU2LAgqMw%26flowName%3DGeneralOAuthFlow%26as%3DS188323732%253A1737569080257578%26client_id%3D717762328687-iludtf96g1hinl76e4lc1b9a82g457nn.apps.googleusercontent.com%26rapt%3DAEjHL4PfDYeoWXR0FbID80yC_q-viZz2XLALKwn12j5eMSJgOnorv9NHleFbQXAwNYiv0hidxy_l7ZM6qCjQTkJNm8zegMYx9uRm8UHCuuxl53b3DYUcQrM%23&tcc=1")
        page.goto("https://accounts.google.com.ng/accounts/SetSID")
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
