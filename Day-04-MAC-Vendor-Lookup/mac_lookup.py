import urllib.request
import json


def get_mac_vendor(mac_address):
  url = f"https://api.macvendors.com/{mac_address}"
  try:
    req = urllib.request.Request(
        url, headers={"User-Agent": "Python-MAC-Lookup"}
    )
    with urllib.request.urlopen(req) as response:
      return response.read().decode("utf-8")
  except urllib.error.HTTPError as e:
    if e.code == 404:
      return "Vendor not found for this MAC address."
    return f"HTTP Error: {e.code}"
  except Exception as e:
    return f"Error: {e}"


def run_mac_lookup():
  print("\n" + "=" * 50)
  print(" MAC Address Vendor Lookup Utility")
  print("=" * 50)

  mac = input("Enter MAC address (e.g., FC:F8:AE:12:34:56): ").strip()

  print(f"\n[*] Looking up vendor for MAC: {mac}...")
  vendor = get_mac_vendor(mac)

  print("\n" + "=" * 50)
  print(f" Manufacturer / Vendor: {vendor}")
  print("=" * 50 + "\n")


if __name__ == "__main__":
  run_mac_lookup()
