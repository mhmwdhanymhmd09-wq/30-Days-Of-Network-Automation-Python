# Day 06: IP to Binary / Hex Converter

A Python-based network utility script designed to convert standard IPv4 addresses into their binary and hexadecimal representations.

## Features
- Converts standard IPv4 decimal addresses into 32-bit binary formats.
- Translates IPv4 addresses into hexadecimal notation.
- Validates input IP formats and handles errors gracefully.

## Requirements
- Python 3.x
- Built-in libraries: `socket`, `struct`

## How to Run
1. Open your terminal or command prompt.
2. Navigate to the `Day-06-IP-Converter` directory.
3. Run the script using the command:
   ```bash
   python ip_converter.py
   ==================================================
 IP to Binary / Hex Converter Utility
==================================================
Enter IPv4 address (e.g., 192.168.1.1): 192.168.1.1

[*] Converting IP address: 192.168.1.1...

==================================================
 Binary Representation : 11000000.10101000.00000001.00000001
 Hexadecimal Representation: 0xC0A80101
==================================================
