from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Launch the browser
        page = browser.new_page()

        # Set custom headers for authorization
        page.set_extra_http_headers({
            "IDNum": "26539148",
            "HebName": "יתיר דוד",
            "HebLastName": "מדר",
            "Mobile": "0545664886",
            "Mail": "eyalst@justice.gov.il",
            "IsNewBo": "true"
        })

        # Go to the URL
        page.goto("http://int-netcore1:8001/")

        # Click the button with text "אזור אישי"
        page.click('text="אזור אישי"')

        # Add a delay or wait for the next page or action to load if needed
        page.wait_for_load_state('networkidle')  # This waits for the network to be idle

        # Optionally, you can take a screenshot to verify the result
        page.screenshot(path="screenshot.png")

        browser.close()

if __name__ == "__main__":
    main()
