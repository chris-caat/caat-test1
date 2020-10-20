from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time

driver = webdriver.Firefox( executable_path=GeckoDriverManager().install() )


# driver = webdriver.Firefox()
driver.get("http://www.caat.org.uk") # put here the adress of your page
elem = driver.find_elements_by_xpath( "//*[@type='submit']" )
# put here the content you have put in Notepad, ie the XPath
# button = driver.find_element_by_id('buttonID') # Or find button by ID.
# print(elem.get_attribute("class"))



# driver.implicitly_wait(10)


timeout = 5
try:
    # accept cookies button:
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
# go to Alternatives page
alternatives_url = 'https://caat.org.uk/alternatives/'
# driver.find_element_by_xpath('//a[@href="'+ alternatives_url +'"]').click()  

# go to Companies page
# <a href="https://caat.org.uk/resources/companies/">Arms companies</a>
companies_url = 'https://caat.org.uk/resources/companies/'

driver.find_element_by_xpath('//a[@href="'+ companies_url +'"]').click()  


# <input id="dh-input-nameSearch-8156859" class="dh-filter-input dh-input-nameSearch" type="text" size="1" placeholder="Company name">

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




# <input id="dh-input-nameSearch-8156859" class="dh-filter-input dh-input-nameSearch" type="text" size="1" placeholder="Company name">
name_input.send_keys( 'Boeing\n' )



time.sleep( 5 )
driver.close()