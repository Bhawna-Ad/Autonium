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
username.send_keys("ad05bhawna@gmail.com")
password.send_keys("@utom@t!on")
time.sleep(2)

# clicking on submit button
submit = driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)

