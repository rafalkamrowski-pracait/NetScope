import re
import subprocess
from .fingerprint import detect_device
from .rules import PORT_RULES


def discover_hosts(target):
    print(f"Discovering hosts in {target}...")
    command = ["nmap", "-sn", target] 
    result = subprocess.run(command, capture_output=True, text=True)

    found_ips = re.findall(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", result.stdout)
    found_ips = list(set(found_ips))
    print(f"Found {len(found_ips)} active hosts.")
    return found_ips




def scan_target(target):
    print(f"Starting port scan on {target}...")
    command = [
    "nmap",
    "-Pn",
    "-F",
    "-sV",
    target
]

    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)

    output = result.stdout

    print("Debug: Znalezione otwarte porty:")
    for line in output.splitlines():
    	if "/tcp" in line and "open" in line:
             print(f" -> {line}") 

    for port, device in PORT_RULES.items():
        if port in output:
             print(f"Possible device type based on port {port}: {device}")

    detect_device(target)
    return output
