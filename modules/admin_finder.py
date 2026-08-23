#!/usr/bin/env python3
import requests

def run():
    print("\n[+] Starting Admin Path Finder...")
    target = input("Enter target URL (e.g. https://example.com): ")
    wordlist = ["admin", "login", "dashboard", "administrator", "panel", "wp-admin", "backup", "yonetim"]
    print("[*] Scanning started... (This may take a moment)")

    for path in wordlist:
        url = f"{target.rstrip('/')}/{path}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code != 404:
                print(f"[+] FOUND! -> {url} (Status: {response.status_code})")
        except requests.exceptions.ConnectionError:
            print(f"[-] Connection error: {url}")
        except requests.exceptions.Timeout:
            print(f"[-] Timeout: {url}")
        except Exception as e:
            print(f"[!] Unexpected error: {url} - {e}")

    print("\n[+] Scan completed!")
    input("Press Enter to return to the main menu...")
