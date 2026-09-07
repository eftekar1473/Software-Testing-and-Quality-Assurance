from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(options=options)

driver.get("https://the-internet.herokuapp.com/nested_frames")

driver.switch_to.frame("frame-top")

#switch to next frame
driver.switch_to.frame("frame-middle")

content=driver.find_element(By.ID, value='content').text
print("Content in middle frame ",content)

driver.switch_to.default_content()

driver.switch_to.frame("frame-bottom")
content_bottom=driver.find_element(By.TAG_NAME, value="body").text
print("Content in bottom ",content_bottom)