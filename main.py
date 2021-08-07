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
submit = driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)

# searching for the button named Message
all_buttons = driver.find_elements_by_tag_name("button")
message_buttons = [btn for btn in all_buttons if btn.text == "Message"]

# click on message button of first connection
message_buttons[0].click()

