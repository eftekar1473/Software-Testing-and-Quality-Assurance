from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://practicetestautomation.com/practice-test-login/")

# Explicit Wait
wait = WebDriverWait(driver, 10)

# Username
username = wait.until(
    EC.visibility_of_element_located((By.ID, "username"))
)
username.send_keys("student")

# Password
password = wait.until(
    EC.visibility_of_element_located((By.ID, "password"))
)
password.send_keys("Password123")

# Login button
login_button = wait.until(
    EC.element_to_be_clickable((By.ID, "submit"))
)
login_button.click()