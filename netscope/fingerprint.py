import subprocess
from netscope.rules import FINGERPRINT_RULES


def detect_device(target):

    print(f"Fingerprinting device {target}...")

    command = [
        "sudo", "nmap",
        "-O",
        "--osscan-limit",
        "--max-os-tries", "1",
        "-T4",
        target
    ]

    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=30)
        output = result.stdout
    except subprocess.TimeoutExpired:
        output = ""
        print(f"\n[!] Ostrzeżenie: Detekcja OS dla {target} przekroczyła czas.")
    except Exception as e:
        output = ""
        print(f"\n[!] Wystąpił błąd: {e}")

    device = "Unknown device"

    for keyword, device_type in FINGERPRINT_RULES.items():

        if keyword.lower() in output.lower():
            device = device_type
            break

    print(f"Device type: {device}")

    return device
