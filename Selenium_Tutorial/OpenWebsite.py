from selenium import webdriver

from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")
