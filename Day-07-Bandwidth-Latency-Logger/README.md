# Day 07: Bandwidth & Latency Logger

A Python-based network monitoring tool designed to continuously log network latency (ping) and track connection stability in real-time.

## Features
- Measures real-time ICMP response latency to a specified host or IP address.
- Handles target reachable/unreachable states gracefully with explicit logs.
- Formats logs with timestamps for network troubleshooting and monitoring.

## Requirements
- Python 3.x
- Built-in libraries: `subprocess`, `platform`, `time`, `datetime`

## How to Run
1. Open your terminal or command prompt.
2. Navigate to the `Day-07-Bandwidth-Latency-Logger` directory.
3. Run the script using the command:
   ```bash
   python latency_logger.py
 ==================================================
 Bandwidth & Latency Logger Utility
==================================================
Enter target host/IP to monitor (default 8.8.8.8): 8.8.8.8

[*] Logging latency for 8.8.8.8. Press Ctrl+C to stop.

Timestamp              | Target          | Status / Latency
-------------------------------------------------------
2026-11-03 04:00:00    | 8.8.8.8         | Connected (24.15 ms)
2026-11-03 04:00:02    | 8.8.8.8         | Connected (23.82 ms)
2026-11-03 04:00:04    | 8.8.8.8         | Connected (25.10 ms)  
