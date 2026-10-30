import ipaddress
import os
import platform
import subprocess
from datetime import datetime


def ping_host(ip):
  param = "-n" if platform.system().lower() == "windows" else "-c"
  command = ["ping", param, "1", "-w", "1000", str(ip)]

  response = subprocess.call(
      command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
  )

  return response == 0


def run_ping_sweeper(subnet_cidr):
  print("\n" + "=" * 50)
  print(f" Network Ping Sweeper Started for: {subnet_cidr}")
  print(f" Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
  print("=" * 50)

  net = ipaddress.ip_network(subnet_cidr, strict=False)
  active_hosts = []

  for ip in net.hosts():
    print(f"[*] Scanning: {ip}...", end="\r")
    if ping_host(ip):
      print(f"[+] Active Host Found: {ip}")
      active_hosts.append(str(ip))

  print("\n" + "=" * 50)
  print(f" Scan Completed! Total Active Hosts: {len(active_hosts)}")
  print("=" * 50 + "\n")


if __name__ == "__main__":
  target_subnet = input(
      "Enter network CIDR to sweep (e.g., 192.168.1.0/24): "
  ).strip()
  run_ping_sweeper(target_subnet)
