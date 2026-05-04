#!/usr/bin/env python3
import re
import subprocess
import shlex
from netscope.fingerprint import detect_device
from netscope.rules import PORT_RULES


G = '\033[92m'
Y = '\033[93m'
R = '\033[91m'
B = '\033[94m'
W = '\033[0m'

def validate_target(target):
    """Walidacja dla bezpieczeństwa (Bandit B603)"""
    if not re.match(r"^[a-zA-Z0-9\.\-/]+$", target):
        raise ValueError(f"Nieprawidłowy cel: {target}")
    return shlex.quote(target)

def discover_hosts(target):
    target = validate_target(target)
    print(f"{B}[*] Szukanie hostów w: {W}{target}...")
    command = ["nmap", "-sn", target] 
    result = subprocess.run(command, capture_output=True, text=True, check=False)

    found_ips = re.findall(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", result.stdout)
    found_ips = list(set(found_ips))
    print(f"{G}[+] Znaleziono {len(found_ips)} aktywnych hostów.{W}")
    return found_ips

def scan_target(target):
    target = validate_target(target)
    print(f"\n{B}[*] Rozpoczynam profesjonalny skan portów: {W}{target}")
    command = ["nmap", "-sS", "-sV", "--top-ports", "50", "-T4", target]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=False) 
        output = result.stdout
        print(f"{G}[+] Skanowanie zakończone sukcesem!{W}\n")
        print(f"{B}{'='*50}{W}")
        print(f"{B}RAPORT SKANOWANIA DLA: {Y}{target}{W}")
        print(f"{B}{'='*50}{W}")

        print(f"\n{Y}Znalezione otwarte porty:{W}")
        found_any = False
        for line in output.splitlines():
            if "/tcp" in line and "open" in line:
                 print(f" {G}[OTWARTY]{W} {line}") 
                 found_any = True

        if not found_any:
            print(f" {R}[!] Nie znaleziono otwartych portów.{W}")

        print(f"\n{Y}Analiza urządzenia:{W}")
        for port, device in PORT_RULES.items():
            if port in output:
                 print(f" {G}»{W} Możliwe urządzenie: {Y}{device}{W} (port {port})")

        detect_device(target)
        print(f"\n{B}{'='*50}{W}")
        return output

    except Exception as e:
        print(f"{R}[-][!] Błąd podczas skanowania: {e}{W}")
        return ""

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="NetScope Scanner")
    parser.add_argument('target', help='Adres IP lub domena do skanowania')
    args = parser.parse_args()
    scan_target(args.target)

