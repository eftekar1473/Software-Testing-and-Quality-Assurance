# ================= SIGN UP TEST =================
# Reads signup_tests.txt and tries each signup on the real website.
# yes = must register (go to login page) , no = must be refused.
# Results are printed AND saved into test_report.txt (open it to read later).

import os
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_FILE = os.path.join(BASE_DIR, "test_report.txt")
TESTS_FILE = os.path.join(BASE_DIR, "signup_tests.txt")

BASE_URL = "http://localhost:5173"
SLOW = 0.6     # small pause so you can WATCH each step (bigger = slower)
WAIT = 2.5     # pause after clicking, to see the result + let the page change

# open Chrome (big window so it is easy to watch)
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(5)

# make the reusable login account (used by the login + UI tests later).
# if it already exists the server refuses it, that is fine.
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
report.write("======== SIGN UP TEST ========\n")

print("======== SIGN UP TEST ========")

# read the test cases and run them one by one
for line in open(TESTS_FILE, encoding="utf-8").readlines():
    line = line.strip()
    if line == "" or line.startswith("#"):
        continue

    # {n} = a new random number , {long} = 256 letters (the "too long" edge)
    line = line.replace("{n}", str(random.randint(1000, 999999)))
    line = line.replace("{long}", "A" * 256)

    box = line.split(",")
    name = box[0].strip()
    student_id = box[1].strip()
    email = box[2].strip()
    password = box[3].strip()
    confirm = box[4].strip()
    department = box[5].strip()
    terms = box[6].strip()
    should_register = box[7].strip()

    # fill the form (only type in a box if we have a value for it)
    driver.get(BASE_URL + "/register")
    time.sleep(SLOW)
    if name != "":
        driver.find_element(By.NAME, "name").send_keys(name)
    if student_id != "":
        driver.find_element(By.NAME, "student_id").send_keys(student_id)
    if email != "":
        driver.find_element(By.NAME, "email").send_keys(email)
    if password != "":
        driver.find_element(By.NAME, "password").send_keys(password)
    if confirm != "":
        driver.find_element(By.NAME, "password_confirmation").send_keys(confirm)
    if department != "":
        driver.find_element(By.NAME, "department").send_keys(department)
    if terms == "yes":
        driver.find_element(By.XPATH, "//input[@data-testid='register-terms-checkbox']").click()
    time.sleep(SLOW)
    driver.find_element(By.XPATH, "//button[@data-testid='register-submit-btn']").click()

    # success sends us to the login page. did that happen?
    time.sleep(WAIT)
    registered = "/login" in driver.current_url
    # the correct signups are important - give them extra time to be sure
    if should_register == "yes" and not registered:
        time.sleep(4)
        registered = "/login" in driver.current_url

    # compare result with what we expected
    if should_register == "yes" and registered:
        result = "PASS | " + email + " | pw: " + password + " -> registered"
        passed = passed + 1
    elif should_register == "no" and not registered:
        result = "PASS | " + email + " | pw: " + password + " -> refused (good)"
        passed = passed + 1
    else:
        result = "FAIL | " + email + " | pw: " + password + " -> WRONG, expected: " + should_register
        failed = failed + 1

    print(result)
    report.write(result + "\n")

print("SIGN UP RESULT:", passed, "passed,", failed, "failed")
report.write("SIGN UP RESULT: " + str(passed) + " passed, " + str(failed) + " failed\n\n")
report.close()
driver.quit()
