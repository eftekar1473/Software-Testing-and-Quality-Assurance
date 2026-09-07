# ================= MAIN UI TEST =================
# Logs in first, then opens each page from main_ui_tests.txt and checks it:
#   right tab title , did not crash , did not throw us back to /login.
#   yes = page must open , no = page must be blocked (admin-only).
# Results are printed AND saved into test_report.txt (open it to read later).

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_FILE = os.path.join(BASE_DIR, "test_report.txt")
TESTS_FILE = os.path.join(BASE_DIR, "main_ui_tests.txt")

BASE_URL = "http://localhost:5173"
SLOW = 2   # small pause so you can WATCH each step (bigger = slower)
WAIT = 8       # how long to wait for a page's title before giving up

# open Chrome (big window so it is easy to watch)
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

# make sure the test account exists
driver.get(BASE_URL + "/register")
time.sleep(SLOW)
driver.find_element(By.NAME, "name").send_keys("Selenium Tester")
driver.find_element(By.NAME, "student_id").send_keys("SEL0000001")
driver.find_element(By.NAME, "department").send_keys("CSE")
driver.find_element(By.NAME, "email").send_keys("selenium.tester@student.nstu.edu.bd")
driver.find_element(By.NAME, "password").send_keys("Test1234")
driver.find_element(By.NAME, "password_confirmation").send_keys("Test1234")
driver.find_element(By.XPATH, "//input[@data-testid='register-terms-checkbox']").click()
driver.find_element(By.XPATH, "//button[@data-testid='register-submit-btn']").click()
time.sleep(3)

# log in with the test account, and wait until we really reach the dashboard
driver.get(BASE_URL + "/login")
time.sleep(SLOW)
driver.find_element(By.NAME, "email").send_keys("selenium.tester@student.nstu.edu.bd")
driver.find_element(By.NAME, "password").send_keys("Test1234")
driver.find_element(By.XPATH, "//button[@data-testid='login-submit-btn']").click()
WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))

passed = 0
failed = 0

# also write everything into a file we can open afterwards
report = open(REPORT_FILE, "a", encoding="utf-8")
report.write("======== MAIN UI TEST ========\n")

print("======== MAIN UI TEST ========")

# open each page and check it
for line in open(TESTS_FILE, encoding="utf-8").readlines():
    line = line.strip()
    if line == "" or line.startswith("#"):
        continue

    box = line.split(",")
    path = box[0].strip()
    title_word = box[1].strip()
    should_open = box[2].strip()

    driver.get(BASE_URL + path)

    # 1) wait until the right word shows in the tab title (up to WAIT seconds)
    title_ok = True
    try:
        WebDriverWait(driver, WAIT).until(EC.title_contains(title_word))
    except:
        title_ok = False

    # 2) did the page crash? 3) did it kick us back to login?
    crashed = "Something went wrong" in driver.find_element(By.TAG_NAME, "body").text
    kicked_out = "/login" in driver.current_url

    opened = title_ok and (not crashed) and (not kicked_out)

    if should_open == "yes" and opened:
        result = "PASS | " + path + " -> opened correctly"
        passed = passed + 1
    elif should_open == "no" and not opened:
        result = "PASS | " + path + " -> blocked (good)"
        passed = passed + 1
    else:
        result = "FAIL | " + path + " -> WRONG, expected: " + should_open
        failed = failed + 1

    print(result)
    report.write(result + "\n")

print("MAIN UI RESULT:", passed, "passed,", failed, "failed")
report.write("MAIN UI RESULT: " + str(passed) + " passed, " + str(failed) + " failed\n\n")
report.close()
driver.quit()
