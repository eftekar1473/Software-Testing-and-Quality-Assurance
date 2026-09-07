from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://jqueryui.com/droppable/")
driver.switch_to.frame(0)

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

action = ActionChains(driver)

action.drag_and_drop(source, target).perform()