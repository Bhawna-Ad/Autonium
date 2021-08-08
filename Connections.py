import time
from selenium import webdriver

# loading linkedin in browser
driver = webdriver.Chrome("C:/Users/.../chromedriver.exe")              # path to chromedriver
driver.get("https://linkedin.com")

# logging in to linkedin
time.sleep(2)
username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")
username.send_keys("user_email")                                        # Linkedin email
password.send_keys("user_password")                                     # Linkedin password
time.sleep(2)

# clicking on submit button
submit = driver.find_element_by_xpath("//button[@type='submit']")
driver.execute_script("arguments[0].click();", submit)
time.sleep(2)

# loading connections page
driver.get("https://www.linkedin.com/search/results/people/?origin=SWITCH_SEARCH_VERTICAL")
time.sleep(2)

all_buttons = driver.find_elements_by_tag_name("button")
connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]

for btn in connect_buttons:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)
    send = driver.find_element_by_xpath("//button[@aria-label = 'Send now']")
    driver.execute_script("arguments[0].click();", send)
    close = driver.find_element_by_xpath("//button[@aria-label = 'Dismiss']")
    driver.execute_script("arguments[0].click();", close)
    time.sleep(2)
