from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://training.qaonlinetraining.com/testPage.php")

country = driver.find_element(By.NAME, "country")

select_country = Select(country)

select_country.select_by_visible_text("France")


skill = driver.find_element(By.NAME, "skill")
select_skill = Select(skill)
select_skill.select_by_value("prg")
# select_skill.select_by_value("prg")