from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/")

driver.find_element(By.XPATH, '//*[@id="ti6dpd"]').send_keys("Selenium")

