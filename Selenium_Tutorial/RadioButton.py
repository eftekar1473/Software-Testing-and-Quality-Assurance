from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Start Chrome
driver = webdriver.Chrome(options=options)

# Open website
driver.get("https://training.qaonlinetraining.com/testPage.php")

# Find the radio button
radio_button = driver.find_element(By.XPATH, "/html/body/form/input[4]")

# Click the radio button
radio_button.click()

# Verify whether it is selected
if radio_button.is_selected():
    print("The test passed")
else:
    print("The test failed")