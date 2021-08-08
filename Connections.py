import time
from selenium import webdriver

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


