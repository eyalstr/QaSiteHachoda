from playwright.sync_api import sync_playwright
import logging
import random
import time  # Import the time module for delay
from datetime import datetime
import random

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
            page.goto("http://qa-srv19core5:8022/")

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

            ##############  פתיחת תיק חרבות ברזל ###########
            # Wait for the "להגשת הבקשה" button to be visible and click it
            logging.info('Waiting for "להגשת הבקשה" button to appear...')
            page.wait_for_selector('span:has-text("להגשת הבקשה")', state='visible', timeout=5000)  # 5 seconds timeout

            # Click the button once it is visible
            logging.info('Clicking on the "להגשת הבקשה" button...')
            page.click('span:has-text("להגשת הבקשה")')

            
            ################  אישור שהתביעה נדחתה בשלב ההגשה ############
            # Wait for the "כן" button to be visible and click it
            logging.info('Waiting for "כן" button to appear...')
            page.wait_for_selector('span.toggle-text:has-text("כן")', state='visible', timeout=5000)  # 5 seconds timeout
            # Wait for the page to load completely
            page.wait_for_load_state('domcontentloaded')  # Wait for DOM to be ready (not just network idle)
    
            # Click the "כן" button
            logging.info('Clicking on the "כן" button...')
            page.click('span.toggle-text:has-text("כן")')

            ################ הכנס מספר תביעה ############
           
            # Wait for the input field with data-cy="textbox_input" to be visible
            logging.info('Waiting for input field with data-cy="textbox_input"...')
            page.wait_for_selector('[data-cy="textbox_input"]', state='visible')

            # Enter the value 512341234 into the input field
            logging.info('Entering value into the input field with data-cy="textbox_input"...')
            page.fill('[data-cy="textbox_input"]', '512341234')

            ################## תקופת זכאות ######################
            # Wait for the combobox element to be visible and available

            logging.info('Waiting for the combobox to be available...')
            page.wait_for_selector('span[role="combobox"]', state='attached', timeout=5000)

            # Ensure that the combobox is visible (element is not hidden)
            logging.info('Waiting for the combobox to be visible...')
            page.wait_for_selector('span[role="combobox"]:visible', timeout=5000)

            # Click the combobox to open the dropdown
            logging.info('Clicking the combobox to open the dropdown...')
            page.click('span[role="combobox"]')

            # Wait for the dropdown list (with the role="listbox") to be visible
            logging.info('Waiting for the dropdown list to be visible...')
            page.wait_for_selector('ul[role="listbox"]:visible', timeout=5000)

            # Select the first item in the list (assuming it's a div with class "list-item-label")
            logging.info('Selecting the first item from the dropdown list...')
            page.click('ul[role="listbox"] div.list-item-label')

            # Wait for the combobox to reflect the selection (this ensures the value is updated)
            logging.info('Waiting for the input field to reflect the selected value...')
            page.wait_for_selector('span[role="combobox"] >> input:checked', timeout=5000)

            logging.info('First item successfully selected and updated in the combobox.')

     

            ################### הכנס תאריך ##################aceholder or selector if needed
            
            from datetime import datetime

            logging.info('Waiting for the calendar component to be visible...')
            page.wait_for_selector('p-calendar:visible', timeout=5000)

            # Wait for the input field inside the calendar to be visible
            logging.info('Waiting for the input field inside the calendar...')
            page.wait_for_selector('input[placeholder="dd/mm/yyyy"]:visible', timeout=5000)

            # Get the current date in the desired format dd/mm/yyyy
            current_date = datetime.now().strftime('%d/%m/%Y')
            logging.info(f'Entering the current date {current_date} in the input field...')

            # Fill the date into the input field
            page.fill('input[placeholder="dd/mm/yyyy"]:visible', current_date)


            # Optional: Add a small delay after clicking the calendar button
            time.sleep(1)

        

            ######################  מחזור עסקאות #############                   

            # Try closing any modal or overlay if present
            
            logging.info('Waiting for the input field with dada-cy="textbox_annualTurnover" to be visible...')

            # Wait for the element with dada-cy="textbox_annualTurnover" to be visible
            page.wait_for_selector('[dada-cy="textbox_annualTurnover"]:visible', timeout=5000)

            # Log message indicating we're about to fill the value
            logging.info('Filling the annual turnover field with value...')

            # Use the fill function to input the value into the input field inside the element with dada-cy="textbox_annualTurnover"
            # Here, you might also want to specify a more specific input field inside the div if needed
            page.fill('[dada-cy="textbox_annualTurnover"] input[data-cy="textbox_input"]', "10000")


            #####################  הבא ######################
            # Click on the "הבא" button
            logging.info('Clicking on the "הבא" button...')
            page.click('span:has-text("הבא")')  # Using the text inside the span to target it

            ###################### סיום #####################

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
