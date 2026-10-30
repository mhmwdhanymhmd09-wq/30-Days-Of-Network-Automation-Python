# Day 02: Network Ping Sweeper

A Python-based utility tool designed to scan a local network subnet and discover active hosts by sending ICMP Echo Request packets.

## Features
- Automatically detects the host operating system to adjust the ping command parameters (`-n` for Windows, `-c` for Linux/macOS).
- Parses CIDR network notation using Python's built-in `ipaddress` library.
- Filters and reports only active, responsive hosts in real time.

## Requirements
- Python 3.x
- Built-in libraries: `ipaddress`, `os`, `platform`, `subprocess`, `datetime`

## How to Run
1. Open your terminal or command prompt.
2. Navigate to the `Day-02-Ping-Sweeper` directory.
3. Run the script using the command:
   ```bash
   python ping_sweeper.py
## Example Output
```text
==================================================
 Network Ping Sweeper Started for: 192.168.1.0/24
 Time: 2026-10-30 21:34:33
==================================================
[+] Active Host Found: 192.168.1.1
[+] Active Host Found: 192.168.1.100
[+] Active Host Found: 192.168.1.104
==================================================
 Scan Completed! Total Active Hosts: 3
==================================================
