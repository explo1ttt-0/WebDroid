#!/usr/bin/env python3
import os
import sys

# ANSI color codes (no external library needed)
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
MAGENTA = '\033[95m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    clear_screen()
    banner = f"""
{RED} __        __   _     ____            _     _
{RED} \ \      / /__| |__ |  _ \ _ __ ___ (_) __| |
{RED}  \ \ /\ / / _ \ '_ \| | | | '__/ _ \| |/ _` |
{RED}   \ V  V /  __/ |_) | |_| | | | (_) | | (_| |
{RED}    \_/\_/ \___|_.__/|____/|_|  \___/|_|\__,_|  by Explo1ttt
{RED}
{YELLOW}          >>> Webdroid v1.0 - Web Hacking Toolkit <<<
{CYAN}   [!] For educational purposes only !!
{CYAN}
    """
    print(banner)

def main_menu():
    while True:
        show_banner()

        print(f"{GREEN}================================================")
        print(f"{CYAN}  Options")
        print(f"{GREEN}================================================")
        print(" 1. Port & Service Scanner")
        print(" 2. Brute Force Attack")
        print(" 3. Quick Vulnerability Scanner (SQLi / XSS)")
        print(" 4. HTML Source Code Saver")
        print(" 5. Admin Path Finder")
        print(f"{RED} 6. Exit")
        print(f"{GREEN}================================================")

        choice = input(f"{YELLOW}[?] Enter your choice (1-6): {RESET}")

        # --- 1. Port Scanner ---
        if choice == '1':
            from modules.port_scanner import run
            run()

        # --- 2. Brute Force ---
        elif choice == '2':
            from modules.bruteforce import run
            run()

        # --- 3. Vulnerability Scanner ---
        elif choice == '3':
            from modules.vuln_scanner import run
            run()
        
        # --- 4. HTML Source Saver ---
        elif choice == '4':
            from modules.html_saver import run
            run()
        
        # --- 5. Admin Path Finder ---
        elif choice == '5':
            from modules.admin_finder import run
            run()
        
        # --- 6. Exit ---
        elif choice == '6':
            print(f"{RED}[!] Exiting... Goodbye!")
            sys.exit(0)
        
        # --- Invalid ---
        else:
            print(f"{RED}[!] ERROR: Please enter a valid number (1-6).")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
