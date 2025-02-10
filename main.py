from playwright.sync_api import sync_playwright
import logging
import random
import time  # Import the time module for delay
from datetime import datetime
import random

# Set up logging
#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.basicConfig(
    filename='error_log.txt',  # Specify the log file name
    level=logging.INFO,        # Set the logging level to INFO
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

file_handler = logging.FileHandler('page_content_log.html', mode='a', encoding='utf-8')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logging.getLogger().addHandler(file_handler)

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
           
            from datetime import datetime

            # Generate the 9-digit value
            current_datetime = datetime.now().strftime('%Y%m%d%H%M')  # Example: 202502091830
            unique_number = '5' + current_datetime[-8:]  # Take only the last 8 digits after '5'

            # Logging for debugging
            logging.info(f'Generated 9-digit number: {unique_number}')

            # Wait for the input field
            logging.info('Waiting for input field with data-cy="textbox_input"...')
            page.wait_for_selector('[data-cy="textbox_input"]', state='visible')

            # Enter the generated 9-digit number
            logging.info(f'Entering value: {unique_number} into the input field...')
            page.fill('[data-cy="textbox_input"]', unique_number)


    ################## תקופת זכאות ######################

    
        # --- WAIT FOR COMBOBOX TO BE ATTACHED AND VISIBLE ---
            logging.info('Waiting for the combobox to be attached...')
            page.wait_for_selector('span[role="combobox"]', state='attached', timeout=5000)

            logging.info('Waiting for the combobox to be visible...')
            page.wait_for_selector('span[role="combobox"]:visible', timeout=5000)

            # --- CLICK TO OPEN THE DROPDOWN ---
            logging.info('Clicking the combobox to open the dropdown...')
            page.click('span[role="combobox"]')

            # --- WAIT FOR THE DROPDOWN LIST TO BE VISIBLE ---
            logging.info('Waiting for the dropdown list to be visible...')
            page.wait_for_selector('ul[role="listbox"]:visible', timeout=5000)

            # --- VERIFY THE NUMBER OF OPTIONS IN THE LIST ---
            options = page.locator('ul[role="listbox"] li')
            option_count = options.count()
            logging.info(f'Found {option_count} options in the dropdown.')

            if option_count == 0:
                logging.error('No options available in the dropdown!')
                return

            # --- RANDOMLY SELECT FIRST OR SECOND ITEM BASED ON TEXT CONTENT ---
            chosen_index = random.choice([1, 2])  # Select index 1 (first) or 2 (second)
            logging.info(f'Randomly selecting option {chosen_index} from the dropdown list...')

            # Select option based on its text content
            if chosen_index == 1:
                option_text = "נובמבר-דצמבר 2023"
            else:
                option_text = "ספטמבר-אוקטובר 2023"

            # Locate the option by text content and click
            option = page.locator(f'ul[role="listbox"] li:has-text("{option_text}")')
            if option.is_visible():
                option.click()
                logging.info(f'Successfully selected option with text: "{option_text}"')
            else:
                logging.error(f'Option with text "{option_text}" is not visible.')
                return

            # --- FORCE SELECTION COMMIT (ENSURE VALUE IS REGISTERED) ---
            logging.info('Triggering events to register selection...')
            page.evaluate('''() => {
                let combobox = document.querySelector('span[role="combobox"]');
                if (combobox) {
                    combobox.dispatchEvent(new Event('change', { bubbles: true }));
                    combobox.dispatchEvent(new Event('blur', { bubbles: true }));
                }
            }''')

            # --- WAIT AND VERIFY SELECTION ---
            logging.info('Verifying if selection persisted...')
            time.sleep(1)  # Wait for UI to update
            selected_value = page.inner_text('span[role="combobox"]')
            logging.info(f'Combo box selected value: "{selected_value.strip()}"')

            if not selected_value.strip():
                logging.error("Dropdown selection did not persist!")


    ################### הכנס תאריך ##################aceholder or selector if needed
            
            from datetime import datetime

            # --- WAIT FOR THE CALENDAR CONTAINER ---
            logging.info('Waiting for the calendar container to be visible...')
            page.wait_for_selector('p-calendar:visible', timeout=5000)

            # --- WAIT FOR THE INPUT FIELD INSIDE THE CALENDAR ---
            logging.info('Waiting for the calendar input field to be visible...')
            page.wait_for_selector('input[placeholder="dd/mm/yyyy"]:visible', timeout=5000)

            # --- CLICK THE CALENDAR BUTTON TO OPEN DATE PICKER ---
            logging.info('Clicking the calendar button to open the date picker...')
            page.click('button.p-datepicker-trigger')

            # --- WAIT FOR THE CALENDAR TO BE VISIBLE ---
            logging.info('Waiting for the calendar pop-up to appear...')
            page.wait_for_selector('.p-datepicker', state='visible', timeout=5000)

            # --- SELECT TODAY'S DATE FROM THE DATE PICKER ---
            logging.info('Selecting today\'s date from the date picker...')
            page.click('.p-datepicker-today')  # Adjust if necessary based on your UI

            # --- FORCE INPUT CHANGE EVENT IF NECESSARY ---
            logging.info('Triggering change event on date field...')
            page.evaluate('''
                let dateInput = document.querySelector('input[placeholder="dd/mm/yyyy"]');
                if (dateInput) {
                    dateInput.dispatchEvent(new Event('input', { bubbles: true }));
                    dateInput.dispatchEvent(new Event('change', { bubbles: true }));
                }
            ''')

            # --- CLICK OUTSIDE TO CONFIRM SELECTION ---
            logging.info('Clicking outside to confirm date selection...')
            page.click('body')  # Ensure the value gets registered

            ##################### תביעה ע"ס ################

            # --- WAIT FOR THE PARENT CONTAINER TO BE PRESENT ---
            logging.info('Waiting for the parent container of the annual turnover field...')
            page.wait_for_selector('[dada-cy="textbox_annualTurnover"]:visible', timeout=5000)

            # --- WAIT FOR THE INPUT FIELD INSIDE THE PARENT ---
            logging.info('Waiting for the actual input field to be visible...')
            page.wait_for_selector('[dada-cy="textbox_annualTurnover"] input[data-cy="textbox_input"]:visible', timeout=5000)

            # --- FILL THE INPUT FIELD WITH 10000 ---
            logging.info('Entering value "10000" into the annual turnover field...')
            page.fill('[dada-cy="textbox_annualTurnover"] input[data-cy="textbox_input"]', '10000')

            # --- TRIGGER EVENTS TO ENSURE VALUE IS REGISTERED ---
            logging.info('Triggering change event to ensure the field registers the input...')
            page.evaluate('''
                let inputField = document.querySelector('[dada-cy="textbox_annualTurnover"] input[data-cy="textbox_input"]');
                if (inputField) {
                    inputField.dispatchEvent(new Event('input', { bubbles: true }));
                    inputField.dispatchEvent(new Event('change', { bubbles: true }));
                }
            ''')

            # --- CLICK OUTSIDE TO CONFIRM SELECTION ---
            logging.info('Clicking outside to confirm the field value...')
            page.click('body')  # Ensures that the entered value gets properly registered


            #####################  הבא ######################
            
            # --- WAIT FOR THE BUTTON CONTAINER TO BE VISIBLE ---
            logging.info('Waiting for the wizard navigation container...')
            page.wait_for_selector('.wizard-navigation-container:visible', timeout=5000)

            # --- WAIT FOR THE "הבא" BUTTON TO BE INTERACTIVE ---
            logging.info('Waiting for the "הבא" (Next) button to be enabled...')
            page.wait_for_selector('button[data-cy="button_wizard_next"]:not([disabled])', timeout=5000)

            # --- CLICK THE BUTTON ---
            logging.info('Clicking the "הבא" (Next) button...')
            page.click('button[data-cy="button_wizard_next"]')

            # --- CONFIRM ACTION ---
            logging.info('"הבא" (Next) button clicked successfully.')


            ######################  בחירת מייצג ############

            logging.info('Waiting for the button to be visible...')
            page.wait_for_selector('button[data-cy="button_toggle_applicantType1"]:visible', timeout=5000)

            logging.info('Clicking on the "עו"ד" button...')
            page.click('button[data-cy="button_toggle_applicantType1"]')

            # Log confirmation
            logging.info('Button "עו"ד" clicked successfully.')

            ######################  פרטי התקשרות  ############
            logging.info('Waiting for the email input field to be visible...')
           # Locate the parent container for the email input field
            email_parent = page.locator('div[dada-cy="textbox_email"]')

            # Locate the input inside the identified parent
            email_input = email_parent.locator('input[data-cy="textbox_input"]')

            # Wait for it to be visible
            email_input.wait_for(state="visible", timeout=5000)

            # Fill in the email
            email_input.fill("eyalst@justice.gov.il")


            logging.info('Waiting for the email verification input field to be visible...')
            page.wait_for_selector('input[data-cy="textbox_input"][id^="emailVerification"]', state='visible', timeout=5000)

            logging.info('Entering email "eyalst@justice.gov.il" into the email verification field...')
            page.fill('input[data-cy="textbox_input"][id^="emailVerification"]', 'eyalst@justice.gov.il')

            logging.info('Email verification entered successfully.')


            logging.info('Waiting for the phone number input field to be visible...')
            page.wait_for_selector('input[data-cy="textbox_input"][id^="phoneNum"]', state='visible', timeout=5000)

            logging.info('Entering phone number "0545664886" into the phone number field...')
            page.fill('input[data-cy="textbox_input"][id^="phoneNum"]', '0545664886')

            logging.info('Phone number entered successfully.')


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
