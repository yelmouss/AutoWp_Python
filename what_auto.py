import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Download and install the ChromeDriver
ChromeDriverManager().install()

# Create the webdriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://web.whatsapp.com/")

# Wait for the page to load
time.sleep(15)

# Search for a specific item
search_box = driver.find_element(By.CSS_SELECTOR, ".input-field--31cXr")
search_box.send_keys("0612865681")

# Wait for 5 seconds
time.sleep(5)

# Click the desired search result
button = driver.find_element_by_xpath("//span[contains(., '0612865681')]")
button.click()

# Wait for 5 seconds
time.sleep(5)

# Enter a message and send it
input_field = driver.find_element_by_class_name("_1Plpp")
input_field.send_keys("Hello, World!")

button = driver.find_element_by_class_name("_35EW6")
button.click()
