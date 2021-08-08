from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


# loading linkedin in browser
driver = webdriver.Chrome("C:/Users/.../chromedriver.exe")
driver.get("https://linkedin.com")


# logging in to linkedin
time.sleep(2)
username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")
username.send_keys("user_email")
password.send_keys("user_password")
time.sleep(2)

# clicking on submit button
submit = driver.find_element_by_xpath("//button[@type='submit']")
driver.execute_script("arguments[0].click();", submit)
time.sleep(2)

# loading connections page
driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&page=")
time.sleep(2)

# searching for the button named Message
all_buttons = driver.find_elements_by_tag_name("button")
message_buttons = [btn for btn in all_buttons if btn.text == "Message"]

# iterating through the message buttons and sending messages
for i in range (0, len(message_buttons)):
    # click on message button of first connection
    driver.execute_script("arguments[0].click();", message_buttons[i])
    time.sleep(2)

    # click on messaging area of the message window
    main_div = driver.find_element_by_xpath("//div[starts-with(@class, 'msg-form__msg-content-container')]")
    driver.execute_script("arguments[0].click();", main_div)

    # searching through the tags
    paragraphs = driver.find_elements_by_tag_name("p")
    # writing the message after the last sent
    paragraphs[-5].send_keys("testing")
    time.sleep(2)
    submit = driver.find_element_by_xpath("//button[@type='submit']")
    driver.execute_script("arguments[0].click();", submit)
    time.sleep(2)

    # closing the message window
    close_button = driver.find_element_by_xpath(
        "//button[starts-with(@data-control-name, 'overlay.close_conversation_window')]")
    driver.execute_script("arguments[0].click();", close_button)
    time.sleep(2)

