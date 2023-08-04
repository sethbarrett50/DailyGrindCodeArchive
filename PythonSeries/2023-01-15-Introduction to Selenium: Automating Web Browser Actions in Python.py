# To use Selenium, you need to install the library and also install a web driver for the browser you want to use. 
# For example, to use Chrome, you need to install the chromedriver executable. 
# Then, you can use the webdriver module to control the browser:
from selenium import webdriver
from selenium.webdriverQ.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()  # start Chrome
driver.get("http://www.example.com")  # navigate to a website
sub_btn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "submit_button"))
)
sub_btn.click()
driver.close()  # close the browser

# Selenium provides a rich API for interacting with web elements such as buttons, links, and forms. ou can use methods such as EC.
# presence_of_element_located() inside a WebDriverWait(driver, 10).until(...) code block to wait for an element to load, then locate the element on the webpage and perform actions on them. 
# Elements can be located with their ID, CLASS_NAME, CSS_SELECTOR, LINK_TEXT, NAME, PARTIAL_LINK_NAME, TAG_NAME or XPATH. 
# For example:
from selenium import webdriver
from selenium.webdriverQ.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.example.com")

# Fill out a form
name_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"//*[@id='name']"))
)
name_box.send_keys("John Smith")
email_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"//*[@id='email']"))
)
email_box.send_keys("jon@example.com")
sub_btn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "submit_button"))
)
sub_btn.click()

# Extract data from the webpage
name  = driver.find_element(By.ID, "name").get_attribute("value")
print(name)  # prints "John Smith"

driver.close()