NetScope is a command-line network scanning tool that automates host discovery, port scanning, and basic service analysis using nmap.

It is built as a learning project to understand how real-world reconnaissance tools work.

✨ Features

🔎 Host discovery

⚡ Fast port scanning

🧠 Service detection (nmap -sV)

🖥️ Basic device fingerprinting

📄 Report generation (netscope_report.txt)

⏱️ Timeout handling (prevents freezing)

🧩 Modular structure (easy to expand)

🖼️ Preview
[*] Starting NetScope...
[+] Found 1 active host

[+] Scanning target: 45.33.32.156
[+] Scan completed

==================================================
SCAN REPORT FOR: 45.33.32.156
==================================================

Open ports:
 [OPEN] 22/tcp  (SSH)
 [OPEN] 80/tcp  (HTTP - Apache)

Device analysis:
 → Linux / SSH device
 → Web server
🛠️ Requirements

Python 3.x

Nmap

Install Nmap (Linux)
sudo apt update
sudo apt install nmap
🚀 Usage
sudo python3 netscope.py --target <IP_or_domain>
Example
sudo python3 netscope.py --target scanme.nmap.org
📄 Output

After scanning, a report is saved to:

netscope_report.txt

View it with:

cat netscope_report.txt

or:

less netscope_report.txt
⚙️ How It Works

Validates target input

Discovers active hosts

Runs Nmap scan (-Pn -F -sV)

Parses open ports

Maps ports to possible device types

Runs optional fingerprinting

Saves results to file

🧱 Project Structure (example)
netscope/
│── netscope.py
│── scanner.py
│── utils.py
│── README.md
🔐 Disclaimer

This tool is intended for educational purposes only.

Do not scan networks, systems, or devices without explicit permission.

🧠 Learning Goals

Understanding network scanning

Working with subprocess in Python

Parsing CLI tool output

Building CLI security tools

Preparing for GUI integration

🚧 Roadmap

GUI version (Tkinter / PyQt)

Export to JSON / HTML

Multi-target scanning

Improved fingerprinting

Logging system

👨‍💻 Author

Created as part of a cybersecurity learning journey.

⭐ Contribute

Feel free to fork, improve, and experiment.

If you like the project — leave a ⭐ on GitHub!
