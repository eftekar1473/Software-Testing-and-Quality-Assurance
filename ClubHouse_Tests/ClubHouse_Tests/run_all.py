# ================= RUN ALL TESTS =================
# Runs the 3 test files and shows ONE final result.
# (In Python, importing a file RUNS it - just like the concept files.
#  After it runs, we read how many passed/failed from each.)
#
# RUN THIS:   python run_all.py     (from inside this folder)
# Results also get saved into test_report.txt (open it to read everything).

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

REPORT_FILE = os.path.join(BASE_DIR, "test_report.txt")

# clear the old report first. (this line runs BEFORE the imports below,
#  so the 3 tests then add their fresh results to an empty file.)
open(REPORT_FILE, "w", encoding="utf-8").close()

# (these 3 are the sibling test files in THIS folder. your editor may show a
#  yellow "could not be resolved" underline - ignore it, it runs fine when you
#  run from inside this folder. "# type: ignore" just hides that editor note.)
import test_signup      # type: ignore
import test_login       # type: ignore
import test_main_ui     # type: ignore

total_passed = test_signup.passed + test_login.passed + test_main_ui.passed
total_failed = test_signup.failed + test_login.failed + test_main_ui.failed
total = total_passed + total_failed
percent = total_passed / total * 100

print()
print("############### FINAL TEST RESULT ###############")
print("Sign up :", test_signup.passed, "passed,", test_signup.failed, "failed")
print("Login   :", test_login.passed, "passed,", test_login.failed, "failed")
print("Main UI :", test_main_ui.passed, "passed,", test_main_ui.failed, "failed")
print("-------------------------------------------------")
print("TOTAL   :", total_passed, "/", total, "=", round(percent, 1), "%")
print("#################################################")

if total_passed == total:
    print("100% -> WEBSITE IS WORKING CORRECTLY.")
else:
    print("NOT 100% -> WEBSITE HAS A BUG. Check the FAIL lines above.")
    print("(the mistake is in the login, signup, or a UI page logic)")

# save the final result into the report file too
report = open(REPORT_FILE, "a", encoding="utf-8")
report.write("############### FINAL TEST RESULT ###############\n")
report.write("Sign up : " + str(test_signup.passed) + " passed, " + str(test_signup.failed) + " failed\n")
report.write("Login   : " + str(test_login.passed) + " passed, " + str(test_login.failed) + " failed\n")
report.write("Main UI : " + str(test_main_ui.passed) + " passed, " + str(test_main_ui.failed) + " failed\n")
report.write("TOTAL   : " + str(total_passed) + " / " + str(total) + " = " + str(round(percent, 1)) + " %\n")
if total_passed == total:
    report.write("100% -> WEBSITE IS WORKING CORRECTLY.\n")
else:
    report.write("NOT 100% -> WEBSITE HAS A BUG.\n")
report.close()

# keep the window open so you can read the result
input("\nPress ENTER to close...")
