from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

options = Options()

options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(options=options)


driver.get("https://www.google.com/")


driver.switch_to.new_window()
driver.get("https://demo.itlearn360.com/")
number_tab = len(driver.window_handles)
print(number_tab)

tab_value = driver.window_handles
print(tab_value)


current_tab = driver.current_window_handle
print(current_tab)


driver.find_element(By.XPATH, '//*[@id="login-list"]/li[2]/a').click()

first_tab = tab_value[1]

if current_tab != first_tab:
    driver.switch_to.window(first_tab)

driver.find_element(By.LINK_TEXT, "Gmail").click()