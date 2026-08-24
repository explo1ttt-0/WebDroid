#!/usr/bin/env python3
import requests
import os
from bs4 import BeautifulSoup

def run():
    print("\n[+] HTML Source Code Saver started.")
    url = input("Enter the URL to download: ")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # BeautifulSoup ile pretty-print yap
        soup = BeautifulSoup(response.text, 'html.parser')
        pretty_html = soup.prettify()
        
        filename = input("Enter filename to save (without extension, e.g. 'index'): ")
        if not filename:
            filename = url.replace("https://", "").replace("http://", "").replace("/", "_")
        filename += ".html"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(pretty_html)
        
        print(f"[+] Successfully saved to {filename} (Size: {len(pretty_html)} characters)")
    
    except requests.exceptions.ConnectionError:
        print("[-] Connection error: Could not reach the URL.")
    except requests.exceptions.Timeout:
        print("[-] Timeout: The server did not respond in time.")
    except requests.exceptions.HTTPError as http_err:
        print(f"[-] HTTP error occurred: {http_err}")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
    
    input("\nPress Enter to return to the main menu...")
