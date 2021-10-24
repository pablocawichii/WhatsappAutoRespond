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
        # xarg = "//div[class='_1i_wG']/../../div[class='_3vPI2']/div[class='zoWT4']/span/span/title"
        xarg = "//span[contains(@aria-label, 'unread messages')]/../../../../..//div[@class='zoWT4']/span"
        det = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((
                By.XPATH,
                xarg
                )))

        out = []
        for i in det:
            title = i.get_attribute("title")
            out.append(title)
            print(title)

        return out
    except TimeoutException:
        return None

# This function responds to a person
# If their name is given
def respond_to_person(driver, person):

    message = "Hello, I am currently busy. Please contact me again in 2 hours."
    try:
        xarg = f"//div[@class='zoWT4']/span[@title='{person}']"
        grp = driver.find_element_by_xpath(xarg)
        grp.click()
        inparg = "//div[@class='_13NKt copyable-text selectable-text'][@data-tab='9']"
        inp = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                inparg
            )))
        inp.click()
        inp.send_keys(message, Keys.ENTER)

        return True
    except ElementNotInteractableException:
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
            person = detect_new_messages(driver)
            if(person is not None):
                for per in person:
                    respond_to_person(driver,per)
            time.sleep(30)
    except KeyboardInterrupt:
        print("Program Closing")
        driver.quit()


if __name__ == "__main__":
    main()
