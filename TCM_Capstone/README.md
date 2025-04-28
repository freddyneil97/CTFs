# TCM Capstone
![alt text](logo.png)
## 1️⃣ Understanding the Objectives  
- Carefully went through the website to understand the scope and goals.
- Identify the key deliverables, such as flags, reports, or specific objectives.
- Determine the rules and constraints of the challenge (e.g., time limits, tools allowed).
- Break down the objectives into smaller, actionable tasks to create a clear plan.

##  2️⃣  Set Up Your Environment  
- Ensure your tools (e.g., Kali Linux, Burp Suite, etc.) are installed and updated.
- Verify network configurations and connectivity.
![main](https://github.com/user-attachments/assets/b158cdad-ae50-4a5d-9ab1-718c3d8fa845)

  

## 3️⃣ Information Gathering  
- Perform reconnaissance using tools like `nmap` for port scanning.
![1](https://github.com/user-attachments/assets/3ba08905-f420-4efa-84db-e36b6a0c6b9e)
- Documenting potential vulnerabilities
### Reflected XXS 
![3](https://github.com/user-attachments/assets/1eb92225-96bc-4c90-a8ca-c1458dc0d51a)
![2](https://github.com/user-attachments/assets/abb81a95-1001-4996-bc81-62593423c0a2)


### Stored XSS
![stored](https://github.com/user-attachments/assets/caac663c-c6e9-4200-b8e5-01b541703336)


### Application allows weak password
When I signed up for a user - it alowed me to sign up with 'test' as the username and the password, and hence may be susceptible to brute force attacks.

### SQL injection
![sql_in](https://github.com/user-attachments/assets/e0d2c67c-4270-4525-9733-92f827246084)



##  4️⃣  Enumeration  
- Use tools like `Gobuster` or `Dirb` to find hidden directories. But I used ffuf
![ffuf](https://github.com/user-attachments/assets/36e75f5a-9344-4ae1-af32-b5bf844a5007)


## 5️⃣  Exploitation  
- Used SQL injection to obtain the user's passwords.
![sqlpass](https://github.com/user-attachments/assets/3a56cf8b-da36-4d1c-a8ed-b2a4e8927dfe)

- Cracked the passwords using 'hashcat'.
In cracking the hashes we need to identify which mode need to be used. We can easily identify the modes in this website - https://hashcat.net/wiki/doku.php?id=example_hashes

Then we used mode in hashcat as follows
```
hashcat -m 3200 hash /usr/share/wordlists/wifite.txt
```
- I also ran `sqlmap` to have a complete understanding of the database
```
sqlmap -r sql.txt -T users --dump

```
![sqlmap](https://github.com/user-attachments/assets/8c93920c-8197-4940-839a-644b15240365)


## 6️⃣  Privilege Escalation  
- Since we have all the password hashes for the users/admins we can login as admins and navigate to the admin panel.
![admin](https://github.com/user-attachments/assets/942060cf-0d9e-43fc-a6f0-00b9d12c02c1)


## 7️⃣  Post-Exploitation  
- From here we can use Insecure file upload to gain remote code execution using burpsuite.

![remote_exp](https://github.com/user-attachments/assets/e7896b51-a53b-41f6-87ab-69aaf86c9d16)
![remote_cmd](https://github.com/user-attachments/assets/16886ec0-9314-48be-abd8-14e99863b084)




## 8️⃣  Cleanup  
- There are no cleanup necessary as this run in docker container in my own system. http://localhost.capstone/init.php will reset the database.

## 9️⃣ Review and Reflect  
- Just because I found one vulnerability does not meet there will not be multiple.
- Think like an ethical hacker and not be lazy.

## Thank You
