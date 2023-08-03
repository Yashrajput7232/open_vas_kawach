from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # Importing 'By' to use in locating elements

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Add this line to run Chrome in headless mode
chrome_options.add_argument("--no-sandbox")  # Required for some cloud environments, including CodeSpaces

# Initialize Chrome WebDriver without 'executable_path' argument
driver = webdriver.Chrome(options=chrome_options)

# Replace 'url_of_form' with the actual URL of the web form
driver.get('https://yashrajput7232-turbo-spork-67j75qq65qx2r444-5500.app.github.dev/selenium/test.html')

# Locate the username input field and fill it with the value "admin"
username_input = driver.find_element(By.NAME, 'username')
username_input.send_keys('admin')

# (Optional) Locate the password input field and fill it with the password value
password_input = driver.find_element(By.NAME, 'password')
password_input.send_keys('your_password')

# (Optional) Submit the form by locating the sign-in button and clicking it
# This step is optional if the form is submitted automatically upon filling the fields
# If you have a login button, you can use it like this:
# login_button = driver.find_element(By.XPATH, '//button[contains(@data-testid, "login-button")]')
# login_button.click()

# Optional: Add some delay to let the user see the filled values before closing the browser
import time
time.sleep(5)

# Close the web driver
driver.quit()
