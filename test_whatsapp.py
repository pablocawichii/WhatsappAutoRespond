import whatsapp
import pytest
from selenium import webdriver
import time

@pytest.fixture(scope="module", autouse=True)
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(60)
    driver.get("https://web.whatsapp.com/")
    return driver


def test_detect_message(driver):
    res = whatsapp.detect_new_messages(driver)
    assert res is not None

def test_detect_no_message(driver):
    res = whatsapp.detect_new_messages(driver)
    assert res is None


def test_respond(driver):
    res = whatsapp.respond_to_person(driver, "CawichHome")
    assert res == True
