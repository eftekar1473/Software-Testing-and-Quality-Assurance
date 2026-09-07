from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.reddit.com/")

driver.find_element(By.NAME, "q").send_keys("Selenium")


driver.find_element(By.CLASS_NAME, "gNO89b").submit()