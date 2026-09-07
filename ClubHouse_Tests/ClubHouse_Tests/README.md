# ClubHouse Selenium Test — README

Selenium diye ClubHouse website **automatic test**. Test case gula **`.txt`
file e** (line by line, **onk gula case — mot 106 ta**). Python file choto +
easy — shudhu txt poRe ar protita line test kore. `Selenium_Session` folder er
concept use kora: Locate By Name, Locate By Xpath, CheckBox, Implicit Wait, `time.sleep`.

---

## File gula

| File | Ki | koyta case |
|------|-----|-----------|
| `login_tests.txt`   | login er test case (email, password, yes/no) | **47** |
| `signup_tests.txt`  | signup er test case (sob field + yes/no) | **45** |
| `main_ui_tests.txt` | login er por je page gula khulbe | **14** |
| `test_login.py`     | `login_tests.txt` poRe run kore | |
| `test_signup.py`    | `signup_tests.txt` poRe run kore | |
| `test_main_ui.py`   | login kore, `main_ui_tests.txt` er page check kore | |
| `run_all.py`        | tin ta ek shathe chalay + **1 ta final result** | |
| `test_report.txt`   | **result gula ekhane save hoy** (run korle toiri hoy) | |

Notun test case add korte chaile — python e hat dewar dorkar nai, shudhu
`.txt` file e notun line likhe dao. `{n}` = random number, `{long}` = 256 letter.

---

## Age: website START koro (2 terminal)

Code ache: `D:\Selenium_Tutorial\ClubHouse-main\ClubHouse-main`

**Terminal 1 — Backend (port 8000):**
```
cd D:\Selenium_Tutorial\ClubHouse-main\ClubHouse-main\backend
php artisan migrate      # first time only
php artisan serve
```
**Terminal 2 — Frontend (port 5173):**
```
cd D:\Selenium_Tutorial\ClubHouse-main\ClubHouse-main\frontend
npm install              # first time only
npm run dev
```
`http://localhost:5173/login` khulle website ready.

---

## Test cholao (aro 1 terminal) — ei folder theke

```
cd D:\Selenium_Tutorial\ClubHouse_Tests

# sob ek shathe (final result soho):
D:\Selenium_Tutorial\.venv\Scripts\python.exe run_all.py

# othoba alada alada:
D:\Selenium_Tutorial\.venv\Scripts\python.exe test_signup.py
D:\Selenium_Tutorial\.venv\Scripts\python.exe test_login.py
D:\Selenium_Tutorial\.venv\Scripts\python.exe test_main_ui.py
```
> **Ei folder er bhitor theke** chalao (txt file gula pete hobe).

---

## Result koi dekhbo?

**2 jaygay:**
1. **Terminal e** — protita line `PASS` ba `FAIL` dekhabe, sesh e final result.
   `run_all.py` sesh e window bondho hoy na (ENTER chapte hoy), tai poRe dekha jay.
2. **`test_report.txt` file e** — same result file e save hoy. Ei file open
   korle sob PASS/FAIL + final % dekha jabe (terminal miss korle o).

Sesh e emon dekhabe:
```
TOTAL   : 106 / 106 = 100.0 %
100% -> WEBSITE IS WORKING CORRECTLY.
```
- **100%** = website thik.
- **kom** = kono test FAIL = website code e **bug** (login/signup/UI logic).

---

## Aste (slow) korte / taratari korte

Protita python file er upore duita line:
```
SLOW = 0.6     # protita step er por choto pause (baralে aro slow)
WAIT = 2.5     # click er por pause (result dekhar jonno)
```
- Aro **aste** (bhalo kore dekhte): `SLOW = 1.5` , `WAIT = 4` koro.
- Aro **taratari**: `SLOW = 0.2` , `WAIT = 1.5` koro.
- Chrome window boro kore khule (`--start-maximized`), tai screen e sob dekha jay.

---

## Boundary Value Analysis (kon edge test korchi)

**Login (47):** valid login; empty email/pass; bhanga email shape
(`rahimuddin`, `rahim.uddin@`, `@student...`, double `@`, space); real naam er
moto email jara register kore nai (must fail); wrong domain (`@gmail.com`);
thik email + **wrong password**; onek choto/boro password; attack-looking (`' OR '1'='1`).

**Sign up (45):**

| edge | input | asha |
|------|-------|------|
| password | 8 char (`Fatima24`) | ok |
| password | 7 char / 3 char / 4 char | refuse |
| password | shudhu letter / shudhu number | refuse |
| confirm | password != confirm | refuse |
| email | `@gmail.com`, `@student.nstu.edu`, `...bd.com` | refuse |
| email | `@student.nstu.edu.bd` | ok |
| name | 256 char (`{long}`) | refuse |
| department | fka / 256 char | refuse |
| required | name/id/email/password fka | refuse |
| terms | tick na kora | refuse |
| duplicate | already-taken email / student id | refuse |

**Main UI (14):**
- Normal page (must open): `/dashboard /clubs /events /announcements /recruitment /notifications /search /profile`
- **Admin page (normal student BLOCKED hobe):** `/admin/users /admin/clubs /admin/audit-logs /admin/reports`
  -> ei gula khulle bug (normal user admin page dekhe felse).
- Unknown page -> **404** page dekhabe.

---

## GURUTTOPURNO: rate limit (server niyom)

Website server **1 minute e maximum 3 ta signup ar 5 ta login** (per email)
allow kore (spam thekano). Tai:
- Valid case gula **first e** rakha ache, tai ek bar chalale sob thik ashe.
- Sathe sathe **abar** chalale valid signup/login FAIL dekhate pare (server "too
  many requests" dey). Eta website er bug **NA**. **1 minute wait** kore abar chalao.

---

## Kaj na korle

- Sob login FAIL → backend (8000) cholche kina dekho.
- Page fka / connection error → frontend (`npm run dev`) cholche kina dekho.
- URL alada (5173 na) → protita py file er upore `BASE_URL` change koro.
- Chrome window dekhte chao na → `options.add_argument("--headless=new")` add koro.
