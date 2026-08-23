Webdroid 

Webdroid is a Python-based web security toolkit designed for learning, experimentation, and authorized security testing.

The project brings together several useful reconnaissance and web security features in a single command-line interface. It is currently in its early stages and will continue to evolve with new modules, improvements, and additional functionality.

Webdroid is also a personal learning project. As the project develops, the goal is not only to add new features, but also to improve the codebase, optimize existing modules, and build a better understanding of how the underlying techniques work.

Features
🔍 Port & Service Scanner

Scan a target for common ports and identify available services.

🔐 Brute Force Module

A module for testing authentication strength in authorized environments.

🛡️ Quick Vulnerability Scanner

Basic checks for common web vulnerabilities, including:

SQL Injection (SQLi)
Cross-Site Scripting (XSS)
📄 HTML Source Code Saver

Retrieve and save the HTML source code of a target page for further analysis.

🔎 Admin Path Finder

Check common administrative paths and directories on a target.

Installation

Clone the repository:

git clone https://github.com/explo1ttt/Webdroid.git

Move into the project directory:

cd Webdroid

Install the required dependencies:

pip install -r requirements.txt

Run the tool:

python3 webdroid.py
Usage

After launching Webdroid, select one of the available modules from the main menu and provide the required target information.

1. Port & Service Scanner
2. Brute Force Module
3. Quick Vulnerability Scanner (SQLi / XSS)
4. HTML Source Code Saver
5. Admin Path Finder
6. Exit
Roadmap

Webdroid is still under development. Some planned improvements include:

 Expanded admin path wordlists
 Improved vulnerability detection
 More accurate result analysis
 Better error handling
 Improved output and reporting
 Additional scanning options
 New modules and features
 Code optimization and refactoring
Disclaimer

⚠️ Webdroid is intended for educational purposes and authorized security testing only.

Only use this tool against systems, applications, or networks that you own or have explicit permission to test.

The developer is not responsible for misuse, unauthorized testing, or damage caused by the use of this software.

Author

Developed and maintained by Explo1ttt
