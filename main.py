from playwright.sync_api import sync_playwright
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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

        try:
            # Go to the URL
            logging.info("Navigating to the website...")
            page.goto("http://int-netcore1:8001/")

            # Click the "אזור אישי" button
            logging.info('Clicking on "אזור אישי" button...')
            page.click('text="אזור אישי"')

            # Wait for the next page or action to load
            page.wait_for_load_state('networkidle')  # This waits for the network to be idle
            logging.info('Page loaded successfully.')

            # Wait for the "פתיחת תיק" button to be visible
            logging.info('Waiting for "פתיחת תיק" button to appear...')
            try:
                page.wait_for_selector('span.ng-tns-c2721708500-7', state='visible', timeout=30000)  # 30-second timeout
                logging.info('Button found and clicked.')
                page.click('text="פתיחת תיק"')
            except Exception as e:
                logging.error(f'Error waiting for selector: {e}')
                logging.info('Page HTML at error point:\n' + page.content())  # Log current page content for debugging
                
            # Add a delay to ensure the action has been processed
            time.sleep(3)  # Adjust this if necessary

            # Optionally, you can take a screenshot to verify the result
            logging.info('Taking a screenshot...')
            #page.screenshot(path="screenshot.png")

            logging.info('Action completed successfully.')
            # Add a delay to ensure the action has been processed
            time.sleep(3)  # Adjust this if necessary

        except Exception as e:
            logging.error(f"An error occurred: {e}")
        finally:
            # Close the browser
            logging.info('Closing the browser...')
            browser.close()

if __name__ == "__main__":
    main()
