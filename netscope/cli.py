import sys
import subprocess
from colorama import Fore, Style, init
# Importujemy Twoje moduły
from netscope.scanner import discover_hosts, scan_target

# Inicjalizacja kolorów (autoreset sprawia, że kolor wraca do normy po każdym print)
init(autoreset=True)

def check_nmap():
    """Sprawdza, czy nmap jest zainstalowany, aby program był niezależny."""
    try:
        subprocess.run(["nmap", "--version"], capture_output=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print(f"{Fore.RED}[!] BŁĄD: Nmap nie jest zainstalowany w systemie!")
        print(f"{Fore.YELLOW}[*] Sugestia: sudo apt update && sudo apt install nmap")
        sys.exit(1)

def main():
    # 1. Sprawdzenie zależności systemowych
    check_nmap()

    print(f"{Fore.CYAN}{Style.BRIGHT}=== NetScope v1.0.0 ===")
    print(f"{Fore.BLUE}[*] Inicjalizacja skanera...")

    target = input(f"{Fore.WHITE}Podaj cel (IP lub zakres, np. 192.168.1.1): {Style.RESET_ALL}")
    
    if not target:
        print(f"{Fore.RED}[!] Nie podano celu. Zamykanie.")
        return

    try:
        # 2. Wykrywanie hostów
        print(f"{Fore.YELLOW}[*] Szukanie aktywnych hostów w {target}...")
        hosts = discover_hosts(target)

        if not hosts:
            print(f"{Fore.RED}[-] Nie znaleziono aktywnych urządzeń.")
            return

        print(f"{Fore.GREEN}[+] Znaleziono hosty: {', '.join(hosts)}")

        # 3. Skanowanie każdego hosta
        for host in hosts:
            print(f"\n{Fore.MAGENTA}--- Skanowanie: {host} ---")
            report = scan_target(host)
            print(f"{Fore.WHITE}{report}")

        print(f"\n{Fore.GREEN}[+] Skanowanie zakończone pomyślnie.")

    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Przerwano przez użytkownika.")
        sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}[!] Wystąpił nieoczekiwany błąd: {e}")

if __name__ == "__main__":
    main()
