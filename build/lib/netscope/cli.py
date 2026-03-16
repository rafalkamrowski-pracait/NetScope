import argparse
from .scanner import discover_hosts, scan_target

def main():
    parser = argparse.ArgumentParser(description="NetScope - Skaner sieciowy z raportem")
    parser.add_argument("--target", required=True, help="Adres IP lub zakres (np. 192.168.1.0/24)")
    args = parser.parse_args()

    target = args.target
    report_name = "netscope_report.txt"

    print("--- NetScope starting ---")
    active_hosts = discover_hosts(target)

    if not active_hosts:
        print("Nie znaleziono żadnych aktywnych urządzeń.")
        return

    with open(report_name, "w") as f:
        f.write(f"--- RAPORT SKANOWANIA NETSCOPE ---\n")
        f.write(f"Cel: {target}\n")
        f.write("-" * 35 + "\n\n")

    for host in active_hosts:
        print(f"\n[+] Skanowanie urządzenia: {host}")
        scan_results = scan_target(host)
        if "open" in scan_results:
            print(f"!!! Znaleziono otwarte usługi na {host} !!!")
            with open(report_name, "a") as f:
                f.write(f"URZĄDZENIE: {host}\n")
                for line in scan_results.splitlines():
                    if "/tcp" in line and "open" in line:
                        f.write(f"  -> {line}\n")
                f.write("-" * 25 + "\n")
        else:
            print(f"Brak otwartych portów na {host} - pomijam w raporcie.")

    print(f"\n--- Skanowanie zakończone. Raport: {report_name} ---")

if __name__ == "__main__":
    main()

