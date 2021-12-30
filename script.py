import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
 
# import secrets from JSON
with open ('./secrets.json') as s:
    __data = json.load(s)
    __user = __data['tempstick_user']
    __pw = __data['tempstick_pw']
    __execute_path = __data['chromedriver_loc']

option = webdriver.ChromeOptions()
option.add_argument('--headless') # don't open a visible window
driver = webdriver.Chrome(__execute_path, options=option) # Execute path is technically deprecated, but this is the easiest way (for now)
 
page = driver.get('https://temperaturestick.com/sensors/') # Getting page HTML through request

# do the login
# TODO remove the hard-coded username and password
driver.find_element(By.NAME, "email").send_keys(__user)
driver.find_element(By.NAME, "password").send_keys(__pw)
driver.find_element(By.CLASS_NAME, "button").submit()

# wait up to 3 seconds for the appropriate class to show up
WebDriverWait(driver,3).until(lambda d: d.find_element(By.CLASS_NAME, "dashboard-lite__current-reading-last-value"))

# page dynamically loads the values, needs a moment to load them into the class
time.sleep(.25)


temp_read = driver.find_element(By.CLASS_NAME, "dashboard-lite__current-reading-last-value").text
time_read = driver.find_element(By.CLASS_NAME, "dashboard-lite__current-reading-last__time").text

print("Temperature: " + temp_read)
print("Last Read: " + time_read)