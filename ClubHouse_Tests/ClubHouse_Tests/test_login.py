# ================= LOGIN TEST =================
# Reads login_tests.txt and tries each login on the real website.
# yes = must reach dashboard , no = must be blocked.
# Results are printed AND saved into test_report.txt (open it to read later).

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_FILE = os.path.join(BASE_DIR, "test_report.txt")
TESTS_FILE = os.path.join(BASE_DIR, "login_tests.txt")

BASE_URL = "http://localhost:5173"
SLOW = 0.6     # small pause so you can WATCH each step (bigger = slower)
WAIT = 2.5     # pause after clicking, to see the result + let the page change

# open Chrome (big window so it is easy to watch)
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

# make sure the test account exists (so the valid login can work).
# if it already exists the server just refuses it, that is fine.
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
time.sleep(WAIT)

passed = 0
failed = 0

# also write everything into a file we can open afterwards
report = open(REPORT_FILE, "a", encoding="utf-8")
report.write("======== LOGIN TEST ========\n")

print("======== LOGIN TEST ========")

# read the test cases and run them one by one
for line in open(TESTS_FILE, encoding="utf-8").readlines():
    line = line.strip()
    if line == "" or line.startswith("#"):
        continue

    box = line.split(",")
    email = box[0].strip()
    password = box[1].strip()
    should_login = box[2].strip()

    # open a fresh login page and type the email + password
    driver.get(BASE_URL + "/login")
    time.sleep(SLOW)
    if email != "":
        driver.find_element(By.NAME, "email").send_keys(email)
    if password != "":
        driver.find_element(By.NAME, "password").send_keys(password)
    time.sleep(SLOW)
    driver.find_element(By.XPATH, "//button[@data-testid='login-submit-btn']").click()

    # wait a moment, then look at the address bar.
    # a correct login moves us to /dashboard.
    time.sleep(WAIT)
    logged_in = "/dashboard" in driver.current_url
    # the ONE correct login is important - give it extra time to be sure
    if should_login == "yes" and not logged_in:
        time.sleep(4)
        logged_in = "/dashboard" in driver.current_url

    if should_login == "yes" and logged_in:
        result = "PASS | " + email + " | login worked"
        passed = passed + 1
    elif should_login == "no" and not logged_in:
        result = "PASS | " + email + " | blocked (good)"
        passed = passed + 1
    else:
        result = "FAIL | " + email + " | WRONG, expected: " + should_login
        failed = failed + 1

    print(result)
    report.write(result + "\n")

print("LOGIN RESULT:", passed, "passed,", failed, "failed")
report.write("LOGIN RESULT: " + str(passed) + " passed, " + str(failed) + " failed\n\n")
report.close()
driver.quit()
