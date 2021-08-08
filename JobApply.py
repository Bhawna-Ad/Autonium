import random
import time

from selenium import webdriver

# loading linkedin in browser
driver = webdriver.Chrome("C:/Users/Bhawna/chromedriver.exe")              # path to chromedriver
driver.get("https://linkedin.com")

# logging in to linkedin
time.sleep(2)
username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")
username.send_keys("ad05bhawna@gmail.com")                                        # Linkedin email
password.send_keys("@utom@t!on")                                                  # Linkedin password
time.sleep(2)

# clicking on submit button
submit = driver.find_element_by_xpath("//button[@type='submit']")
driver.execute_script("arguments[0].click();", submit)
time.sleep(2)

# loading jobs page
driver.get("https://www.linkedin.com/jobs/")
time.sleep(2)

# finding the search field
search_keywords = driver.find_element_by_xpath("//input[@id='jobs-search-box-keyword-id-ember40']")
search_keywords.clear()
# putting the job keyword
search_keywords.send_keys("Software Engineer")

# finding the location field
search_location = driver.find_element_by_xpath("//input[@id='jobs-search-box-location-id-ember40']")
search_location.clear()
# putting the location
search_location.send_keys("India")
