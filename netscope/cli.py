import sys
import subprocess
from netscope.vulnerability_manager import CVEAnalyzer
from colorama import Fore, Style, init
from netscope.scanner import discover_hosts, scan_target

init(autoreset=True)

def check_nmap():
    """Sprawdza, czy nmap jest zainstalowany, aby program był niezależny."""
    try:
        subprocess.run(["nmap", "--version"], capture_output=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print(f"{Fore.RED}[!] BŁĄD: Nmap nie jest zainstalowany w systemie!")
        print(f"{Fore.YELLOW}[*] Sugestia: sudo apt update && sudo apt install nmap")
        sys.exit(1)

def check_privileges():
    """Sprawdza, czy program ma uprawnienia roota (wymagane dla pełnego skanowania Nmap)."""
    if os.geteuid() != 0:
        print(f"{Fore.YELLOW}[!] Uwaga: Niektóre funkcje Nmapa (np. skanowanie SYN) wymagają uprawnień sudo.")
        print(f"{Fore.YELLOW}[*] Sugestia: Uruchom program jako: sudo python3 cli.py\n")


def main():
    check_nmap()

    print(f"{Fore.CYAN}{Style.BRIGHT}=== NetScope v1.0.0 ===")
    print(f"{Fore.BLUE}[*] Inicjalizacja skanera...")
    analyzer = CVEAnalyzer()

    target = input(f"{Fore.WHITE}Podaj cel (IP lub zakres, np. 192.168.1.1): {Style.RESET_ALL}")
    
    if not target:
        print(f"{Fore.RED}[!] Nie podano celu. Zamykanie.")
        return

    try:
        print(f"{Fore.YELLOW}[*] Szukanie aktywnych hostów w {target}...")
        hosts = discover_hosts(target)

        if not hosts:
            print(f"{Fore.RED}[-] Nie znaleziono aktywnych urządzeń.")
            return

        print(f"{Fore.GREEN}[+] Znaleziono hosty: {', '.join(hosts)}")

        for host in hosts:
            print(f"\n{Fore.MAGENTA}--- Skanowanie: {host} ---")
            report = scan_target(host)
            print(f"\n{Fore.YELLOW}[!] ANALIZA ZAGROŻEŃ NETSCOPE DLA {host}:{Style.RESET_ALL}")
            
            import re
            from rules import PORT_RULES # Upewnij się, że ścieżka do rules jest poprawna
            
            findings = re.findall(r"(\d+)/tcp\s+open\s+\S+\s*(.*)", report)
            
            if not findings:
                # Jeśli nmap nie zwrócił wersji, szukamy samych portów
                simple_ports = re.findall(r"(\d+)/tcp\s+open", report)
                findings = [(p, "Brak szczegółów wersji") for p in simple_ports]

            for port, version in findings:
                key = f"{port}/tcp"
                if key in PORT_RULES:
                    desc = PORT_RULES[key]
                    color = Fore.RED if any(word in desc for word in ["[KRYTYCZNE]", "[WYSOKIE]"]) else Fore.YELLOW
                    print(f"{color} [ALERT] Port {port}: {desc}{Style.RESET_ALL}")
                    if version.strip():
                        print(f"{Fore.WHITE}       └── Wykryto: {version}{Style.RESET_ALL}")
                        print(f"{Fore.CYAN}      [i] Szukam podatności dla: {version}...")
                        cve_results = analyzer.get_cves_by_product(version)
                        print(analyzer.format_report(cve_results))

                else:
                    print(f"{Fore.GREEN} [+] Port {port}: {version if version.strip() else 'Usługa standardowa'}{Style.RESET_ALL}")

        print(f"\n{Fore.GREEN}[+] Skanowanie zakończone pomyślnie.")

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Przerwano przez użytkownika.")
        sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}[!] Wystąpił nieoczekiwany błąd: {e}")

if __name__ == "__main__":
    main()
