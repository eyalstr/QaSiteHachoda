from playwright.sync_api import sync_playwright
import logging
import time  # Import the time module for delay

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

            # Wait for the "אזור אישי" button to be visible and click it
            logging.info('Clicking on "אזור אישי" button...')
            page.click('text="אזור אישי"')

            # Wait for the page to load completely
            page.wait_for_load_state('domcontentloaded')  # Wait for DOM to be ready (not just network idle)

            ############## פתיחת תיק -1 ################

            # Wait for the "פתיחת תיק" button to appear in the side panel
            logging.info('Waiting for "פתיחת תיק" button to appear...')
            page.wait_for_selector('text="פתיחת תיק"', state='visible', timeout=5000)  # 5 seconds timeout

            # Click the button once it is visible
            logging.info('Clicking on the "פתיחת תיק" button...')
            page.click('text="פתיחת תיק"')

            ############## בחירה של חרבות ברזל מתוך רשימה -2 ################
             # Wait for the dropdown to be clickable and open it
            logging.info('Waiting for the dropdown to be visible...')
            page.wait_for_selector('span[role="combobox"]', state='visible', timeout=5000)  # Adjust timeout if needed
            page.click('span[role="combobox"]')  # Open the dropdown

            # Wait for the specific option to be visible and click it
            logging.info('Selecting "ועדת ערר קורונה וחרבות ברזל" from the dropdown...')
            page.wait_for_selector('div.list-item-label[title="ועדת ערר קורונה וחרבות ברזל"]', state='visible', timeout=5000)
            page.click('div.list-item-label[title="ועדת ערר קורונה וחרבות ברזל"]')  # Click the specific item
    
            #################  פתיחת תיק בפועל ##############

            # Wait for the "פתיחת תיק חדש" button to appear and click it
            logging.info('Waiting for the "פתיחת תיק חדש" button...')
            page.wait_for_selector('span:has-text("פתיחת תיק חדש")', state='visible', timeout=5000)  # Wait for the "פתיחת תיק חדש" button

            # Click the "פתיחת תיק חדש" button
            logging.info('Clicking on the "פתיחת תיק חדש" button...')
            page.click('span:has-text("פתיחת תיק חדש")')

            # Optionally, you can take a screenshot to verify the result
            logging.info('Taking a screenshot after clicking the button...')
            page.screenshot(path="submitted_screenshot.png")

            logging.info('Action completed successfully.')

            # Add a delay before closing the browser
            logging.info('Waiting for 5 seconds before closing the browser...')
            time.sleep(5)  # Delay for 5 seconds

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            logging.info('Page HTML at error point:\n' + page.content())  # Log current page content for debugging

        finally:
            # Close the browser
            logging.info('Closing the browser...')
            browser.close()

if __name__ == "__main__":
    main()
