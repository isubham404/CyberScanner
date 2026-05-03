# 🔐 CyberScanner — Mini Web Recon & Vulnerability Scanner


## 👨‍💻 Author

Subham Kar  
B.Tech CSE (CyberSecurity)
GitHub: https://github.com/isubham404/

A beginner-friendly cybersecurity project that automates **reconnaissance and basic vulnerability scanning** using industry tools like Nmap, Gobuster, and Nikto.

---

## 📌 Project Overview

CyberScanner is a Python-based automation tool that performs:

* 🔎 Network scanning (open ports & services)
* 📁 Directory brute-forcing
* ⚠️ Basic web vulnerability detection
* 📝 Automated report generation

This project is designed to simulate a **real-world penetration testing workflow**.

---

## 🧠 How It Works

```
Target Input
   ↓
Nmap Scan (Ports & Services)
   ↓
Gobuster (Hidden Directories)
   ↓
Nikto (Vulnerability Scan)
   ↓
Python Parser
   ↓
Markdown Report
```

---

## ⚙️ Tools Used

* Nmap → Network scanning
* Gobuster → Directory brute-forcing
* Nikto → Web vulnerability scanning
* Python → Automation & parsing

---

## 🚀 Features

* CLI-based scanner
* Automated tool execution
* Output parsing for key findings
* Organized output storage
* Timestamp-based report generation

---

## 📂 Project Structure

```
CyberScanner/
│
├── scanner.py
├── wordlists/
│   └── common.txt
│
├── outputs/
│   ├── nmap.txt
│   ├── gobuster.txt
│   └── nikto.txt
│
├── reports/
│   └── report_<timestamp>.md
│
└── README.md
```

---

## 🖥️ Installation Guide

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/yourusername/CyberScanner.git
cd CyberScanner
```

---

### 🔹 2. Install Python

Make sure Python 3 is installed:

```bash
python3 --version
```

---

### 🔹 3. Install Required Tools

#### ✅ Recommended: Use Kali Linux or WSL

Install:

```bash
sudo apt update
sudo apt install nmap gobuster nikto
```

---

### 🔹 Verify Installation

```bash
nmap --version
gobuster version
nikto -Version
```

---

## 📁 Wordlist Setup

Create:

```
wordlists/common.txt
```

Example content:

```
admin
login
dashboard
panel
api
config
backup
uploads
assets
test
dev
private
logs
```

---

## ▶️ Usage

Run the scanner:

```bash
python3 scanner.py --target https://example.com
```

---

## 📊 Sample Output

```
[+] Starting scan on https://example.com
[+] running : nmap -sV example.com
[+] running : gobuster dir -u https://example.com -w wordlists/common.txt
[+] running : nikto -h https://example.com
[+] Parsing results...
[+] Report saved: reports/report_2026-xx-xx_xx-xx-xx.md
```

---

## 📝 Sample Report

```md
# Scan Report

## Target
https://example.com

## Open Ports
- 80/tcp open http
- 443/tcp open https

## Directories Found
- /admin
- /login

## Vulnerabilities
- Missing security headers
- Outdated server detected
```

---

## ⚠️ Legal Disclaimer

This tool is for **educational purposes only**.

Do NOT scan:

* Unauthorized websites
* Government or private systems without permission

Use only on:

* Your own systems
* Practice labs (TryHackMe, Hack The Box)

---

## 🧠 Learning Outcomes

By building this project, you understand:

* Reconnaissance workflow
* Tool integration
* Output parsing
* Report generation
* Real-world pentesting basics

---

## 🚀 Future Improvements

* Add colored terminal output
* Add subdomain enumeration
* Improve parsing accuracy
* Add GUI interface
* Export reports in HTML/PDF

---

## 👨‍💻 Author

Subham Kar
Cybersecurity Student 🚀

---

## ⭐ Contribute

Feel free to fork, improve, and submit pull requests!

---

## 📌 Final Note

This project is not about hacking — it's about **understanding how systems are tested and secured**.

---
