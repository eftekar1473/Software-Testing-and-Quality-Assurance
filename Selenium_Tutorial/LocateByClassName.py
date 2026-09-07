from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.reddit.com/")

all_links = driver.find_elements(By.TAG_NAME, "a")

for link in all_links:
    url=link.get_attribute("href")
    print(url)

print(len(all_links))
