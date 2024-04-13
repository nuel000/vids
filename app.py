from playwright.sync_api import sync_playwright
import time

# Define a function to run Playwright
def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(1000000)

    # Take a screenshot after page.goto
    page.goto(f"https://web.facebook.com/ads/library/?id={item}")
    page.screenshot(path="screenshot_after_goto.png")

    # Wait for the page to load
    page.wait_for_load_state('load')

    # Take a screenshot after the page finishes loading
    page.screenshot(path="screenshot_after_load.png")

    # Continue with your code...


# Main function
def main():
    # Initialize Playwright
    with sync_playwright() as playwright:
        run(playwright)


if __name__ == "__main__":
    main()
