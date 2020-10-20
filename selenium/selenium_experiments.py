from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time

from selenium.webdriver.firefox.options import Options

ff_options = Options()
ff_options.headless = True

driver = webdriver.Firefox( options=ff_options, executable_path=GeckoDriverManager().install() )

driver.get("http://www.caat.org.uk") 
elem = driver.find_elements_by_xpath( "//*[@type='submit']" )

# click accept cookies button when present
timeout = 5
try:
    element_present = EC.presence_of_element_located(( By.ID, 'ccc-recommended-settings' ))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print( "Timed out waiting for page to load" )
rec_settings_button = driver.find_element_by_id( 'ccc-recommended-settings' )
while True:
    if rec_settings_button.is_displayed():
        break
    time.sleep( 1 )
    print( "blip")
rec_settings_button.click()

# go to Companies page
companies_url = 'https://caat.org.uk/resources/companies/'
driver.find_element_by_xpath('//a[@href="'+ companies_url +'"]').click()  

# go to name INPUT
timeout = 15
try:
    element_present = EC.presence_of_element_located((By.CLASS_NAME, 'dh-input-nameSearch'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print( "Timed out waiting to get element" )

name_input = driver.find_element( By.CLASS_NAME, 'dh-input-nameSearch' )
while True:
    if name_input.is_displayed():
        break
    time.sleep( 1 )
    print( "blip")


# search on "Boeing"
name_input.send_keys( 'Boeing\n' )


time.sleep( 5 )


print( '... closing')
driver.close()