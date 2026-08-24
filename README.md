# 📱 WebDroid

<p align="center">
  <img src="https://github.com" alt="WebDroid Banner" width="800">
</p>

WebDroid is a Python-based web security toolkit designed for learning, experimentation, and authorized penetration testing. It brings several useful reconnaissance and web security features together under a single, user-friendly command-line interface.

This project is also a personal learning journey aimed at improving code quality, optimizing security modules, and deeply understanding network and web vulnerabilities.

---

## 🚀 Features

*   **🔍 Port & Service Scanner:** Scan target hosts for open ports and banners to identify running services.
*   **🔐 Brute Force Module:** Test authentication strength against target forms or protocols in authorized environments.
*   **🛡️ Quick Vulnerability Scanner:** Automated basic checks for common web flaws:
    *   SQL Injection (SQLi)
    *   Cross-Site Scripting (XSS)
*   **📄 HTML Source Code Saver:** Fetch and download the HTML source code of any target web page for offline analysis.
*   **🔎 Admin Path Finder:** Scan and locate hidden administrative panels or common server directories.

---

## 🛠️ Installation & Setup

Follow these steps to clone the repository, install the necessary dependencies, and run the security toolkit on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/explo1ttt-0/WebDroid
```

### 2. Move into the Directory
```bash
cd WebDroid
```

### 3. Install Dependencies
Make sure you have Python 3 and pip installed. Run the following command to download all required modules:
```bash
pip3 install -r requirements.txt
```

### 4. Run the Tool
```bash
python3 main.py
```

---

## 📖 Usage

After launching WebDroid, a command-line interface menu will appear. Simply select the number of the module you wish to use and follow the prompt instructions to provide target details (IP or URL):

1. Port & Service Scanner
2. Brute Force Module
3. Quick Vulnerability Scanner (SQLi / XSS)
4. HTML Source Code Saver
5. Admin Path Finder
6. Exit

---

## 🗺️ Roadmap

WebDroid is under active development. Upcoming milestones include:
- [ ] Expanded and customizable admin path wordlists.
- [ ] Advanced vulnerability detection payloads.
- [ ] Multithreading support for faster scanning speeds.
- [ ] Comprehensive HTML/JSON report generation.
- [ ] Code optimization and robust error handling.

---

## ⚠️ Disclaimer

**WebDroid is intended for educational purposes and authorized security testing only.**  
Only deploy this tool against systems, networks, or applications that you legally own or have explicit written permission to test. The developer assumes absolutely no liability for misuse, unauthorized activities, or legal damages caused by this software.

---

## 👤 Author

*   **Developed and maintained by:** [Explo1ttt](https://github.com)
