import socket
import struct

def ip_to_bin_hex(ip_address):
    try:
        packed_ip = socket.inet_aton(ip_address)
        ip_int = struct.unpack("!I", packed_ip)[0]
        
        binary_ip = ".".join(format(int(octet), "08b") for octet in ip_address.split("."))
        hex_ip = "".join(format(int(octet), "02X") for octet in ip_address.split("."))
        
        return binary_ip, hex_ip
    except socket.error:
        return None, None

def run_ip_converter():
    print("=" * 50)
    print(" IP to Binary / Hex Converter Utility")
    print("=" * 50)
    
    ip = input("Enter IPv4 address (e.g., 192.168.1.1): ").strip()
    
    print(f"\n[*] Converting IP address: {ip}...")
    binary_res, hex_res = ip_to_bin_hex(ip)
    
    print("\n" + "=" * 50)
    if binary_res and hex_res:
        print(f" Binary Representation : {binary_res}")
        print(f" Hexadecimal Representation: 0x{hex_res}")
    else:
        print("[-] Error: Invalid IPv4 address format!")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    run_ip_converter()
