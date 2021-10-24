import whatsapp
import pytest
from selenium import webdriver
import time

# Fixture to run before other tests
# Ensures only one instance of Whatsapp is used
@pytest.fixture(scope="module", autouse=True)
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(60)
    driver.get("https://web.whatsapp.com/")
    return driver


# Test passes if there is a new message
def test_detect_message(driver):
    res = whatsapp.detect_new_messages(driver)
    assert res is not None

# Test passes if there are no new messages
def test_detect_no_message(driver):
    res = whatsapp.detect_new_messages(driver)
    assert res is None

# Test passes if a message is succesfully sent to a specific person
def test_respond(driver):
    person = "Name of Friend/Group" # Change to person to message
    res = whatsapp.respond_to_person(driver, person)
    assert res == True
