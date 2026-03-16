import subprocess
from netscope.rules import FINGERPRINT_RULES


def detect_device(target):

    print(f"Fingerprinting device {target}...")

    command = [
        "nmap",
        "-O",
        "--osscan-limit",
        target
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    output = result.stdout

    device = "Unknown device"

    for keyword, device_type in FINGERPRINT_RULES.items():

        if keyword.lower() in output.lower():
            device = device_type
            break

    print(f"Device type: {device}")

    return device
