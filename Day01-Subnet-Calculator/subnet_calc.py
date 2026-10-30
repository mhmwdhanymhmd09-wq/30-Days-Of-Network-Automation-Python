import ipaddress
import sys

def calculate_subnet(cidr):
    try:
        net = ipaddress.ip_network(cidr, strict=False)
        hosts = list(net.hosts())

        print("\n" + "=" * 40)
        print(f" 🌐 Subnet Analysis for: {net}")
        print("=" * 40)
        print(f"[-] Network Address : {net.network_address}")
        print(f"[-] Netmask         : {net.netmask}")
        print(f"[-] Wildcard Mask   : {net.hostmask}")
        print(f"[-] Broadcast Address: {net.broadcast_address}")
        print(f"[-] Total IP Addresses: {net.num_addresses}")
        print(f"[-] Usable Hosts    : {len(hosts)}")

        if hosts:
            print(f"[-] First Usable IP : {hosts[0]}")
            print(f"[-] Last Usable IP  : {hosts[-1]}")
        else:
            print(f"[-] Usable Hosts    : None")

        print(f"[-] Is Private IP   : {'Yes' if net.is_private else 'No'}")
        print("=" * 40 + "\n")

    except ValueError as e:
        print(f"\n[!] Error: Invalid CIDR notation ({e})\n")

if __name__ == "__main__":
    print("--- Python Network Automation: Day 01 ---")
    if len(sys.argv) > 1:
        target_subnet = sys.argv[1]
    else:
        target_subnet = input("Enter network CIDR (e.g., 192.168.1.0/24): ").strip()

    calculate_subnet(target_subnet)