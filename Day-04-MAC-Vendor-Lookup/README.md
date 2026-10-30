# Day 04: MAC Address Vendor Lookup

A Python-based utility script designed to query a hardware MAC address against online vendor databases to identify the network interface card (NIC) manufacturer.

## Features
- Connects to external MAC vendor lookup APIs efficiently.
- Parses JSON/text responses to extract manufacturer names.
- Handles HTTP errors and missing vendor records gracefully.

## Requirements
- Python 3.x
- Built-in libraries: `urllib.request`, `json`

## How to Run
1. Open your terminal or command prompt.
2. Navigate to the `Day-04-MAC-Vendor-Lookup` directory.
3. Run the script using the command:
   ```bash
   python mac_lookup.py
   ==================================================
 MAC Address Vendor Lookup Utility
==================================================
Enter MAC address (e.g., FC:F8:AE:12:34:56): FC:F8:AE:12:34:56

[*] Looking up vendor for MAC: FC:F8:AE:12:34:56...

==================================================
 Manufacturer / Vendor: Apple, Inc.
==================================================
