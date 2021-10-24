# Import the webdriver
from selenium import webdriver
# Import the keys, to use Keys.Enter
from selenium.webdriver.common.keys import Keys
# Enter Timeout Exception for being unable to
# find any new messages
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
# Used for Explicit Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Used for sleep
import time

# This function is to detect any new messages
# Returns the name of chat if any
def detect_new_messages(driver):
    try:
        # Looks for any unread messages
        xarg = "//span[contains(@aria-label, 'unread messages')]/../../../../..//div[@class='zoWT4']/span"
        det = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((
                By.XPATH,
                xarg
                )))

        #  Gets the name of the groups with unread messages
        out = []
        for i in det:
            title = i.get_attribute("title")
            out.append(title)

        # Returns the list of unread messages
        return out
    except TimeoutException:
        # Returns None if there are no unread messages
        return None

# This function responds to a person
# If their name is given
def respond_to_person(driver, person):

    # The message to be sent
    message = "Hello, I am currently busy. Please contact me again in 2 hours."
    try:
        # Opens the Chat for the person to message
        xarg = f"//div[@class='zoWT4']/span[@title='{person}']"
        grp = driver.find_element_by_xpath(xarg)
        grp.click()

        # Sends the Message after waiting for the input
        inparg = "//div[@class='_13NKt copyable-text selectable-text'][@data-tab='9']"
        inp = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                inparg
            )))
        inp.click()
        inp.send_keys(message, Keys.ENTER)

        # Returns true if succesful
        return True
    except (ElementNotInteractableException, TimeoutException):
        # Returns false if person not found or input could not be found
        return False

# This is the main function
# runs when whatsapp.py is run
def main():
    # Create the driver
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("https://web.whatsapp.com/")
    # Run until stopped
    try:
        while True:
            # Detect any messages and save all that need responding
            person = detect_new_messages(driver)
            if(person is not None):
                # Respond one at a time
                for per in person:
                    respond_to_person(driver,per)
            # Wait for 30 seconds before looking again.
            # There is no need to search every second
            time.sleep(30)
    # Allows a clean exit of the program usign ctrl+c
    except KeyboardInterrupt:
        print("Program Closing")
        driver.quit()


# Runs only when main program
if __name__ == "__main__":
    main()
