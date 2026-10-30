# Day 03: TCP Port Scanner

A Python-based network utility script designed to scan a target IP address or hostname for open TCP ports using socket connections and timeout configurations.

## Features
- Validates and resolves target hostnames to IP addresses.
- Scans a specified range of ports efficiently with a custom connection timeout.
- Identifies active open ports and compiles a summary report.

## Requirements
- Python 3.x
- Built-in libraries: `socket`, `datetime`

## How to Run
1. Open your terminal or command prompt.
2. Navigate to the `Day-03-Port-Scanner` directory.
3. Run the script using the command:
   ```bash
   python port_scanner.py
   ```text
==================================================
 Python TCP Port Scanner
 Time: 2026-10-30 22:00:00
==================================================
Enter target IP or hostname to scan (e.g., 127.0.0.1): 127.0.0.1
Enter start port (e.g., 1): 1
Enter end port (e.g., 1024): 100

[*] Starting scan on target: 127.0.0.1
[*] Please wait, scanning ports...

[+] Port 80 is OPEN
[+] Port 443 is OPEN

==================================================
 Scan Completed! Total Open Ports Found: 2
 Open Ports List: [80, 443]
==================================================
