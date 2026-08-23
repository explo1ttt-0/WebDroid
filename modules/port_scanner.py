#!/usr/bin/env python3
import socket
import sys

def run():
    print("\n[+] Starting Port & Service Scanner...")
    target = input("Enter target IP or domain (e.g. 192.168.1.1 or example.com): ")
    
    ports = {
        21: "FTP",
        22: "SSH",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
        443: "HTTPS",
        3306: "MySQL",
        3389: "RDP",
        5432: "PostgreSQL",
        8080: "HTTP-Alt",
        8443: "HTTPS-Alt"
    }
    
    print(f"[*] Scanning {target}...")
    print("[*] This may take a few seconds...\n")
    
    open_ports = []
    
    for port in ports.keys():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1.5)
            result = sock.connect_ex((target, port))
            sock.close()
            
            if result == 0:
                service = ports[port]
                print(f"[+] Port {port} is OPEN   -> {service}")
                open_ports.append((port, service))
            else:
                print(f"[-] Port {port} is CLOSED -> {ports[port]}")
                
        except socket.gaierror:
            print(f"[!] Invalid hostname or IP address: {target}")
            input("Press Enter to return to the main menu...")
            return
        except KeyboardInterrupt:
            print("\n[!] Scan interrupted by user.")
            input("Press Enter to return to the main menu...")
            return
        except Exception as e:
            print(f"[!] Unexpected error on port {port}: {e}")
    
    print("\n[+] Scan completed!")
    if open_ports:
        print("[+] Open ports found:")
        for port, service in open_ports:
            print(f"    -> {port}: {service}")
    else:
        print("[-] No open ports found.")
    
    input("\nPress Enter to return to the main menu...")
