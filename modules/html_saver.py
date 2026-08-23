#!/usr/bin/env python3
import requests
import os

def run():
    print("\n[+] HTML Source Code Saver started.")
    url = input("Enter the URL to download: ")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Eğer 4xx veya 5xx hatası varsa exception fırlat.
        
        # Kullanıcıdan dosya adı isteyelim
        filename = input("Enter filename to save (without extension, e.g. 'index'): ")
        if not filename:
            # Eğer boş bırakırsa URL'den otomatik isim oluşturalım
            filename = url.replace("https://", "").replace("http://", "").replace("/", "_")
        filename += ".html"
        
        # Dosyayı yaz
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        print(f"[+] Successfully saved to {filename} (Size: {len(response.text)} characters)")
    
    except requests.exceptions.ConnectionError:
        print("[-] Connection error: Could not reach the URL.")
    except requests.exceptions.Timeout:
        print("[-] Timeout: The server did not respond in time.")
    except requests.exceptions.HTTPError as http_err:
        print(f"[-] HTTP error occurred: {http_err}")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
    
    input("\nPress Enter to return to the main menu...")
