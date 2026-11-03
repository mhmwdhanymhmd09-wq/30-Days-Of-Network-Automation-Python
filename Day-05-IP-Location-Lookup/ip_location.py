import json
import urllib.request


def get_ip_location(ip_address):
  url = f"http://ip-api.com/json/{ip_address}"
  try:
    with urllib.request.urlopen(url) as response:
      data = json.loads(response.read().decode("utf-8"))
      if data.get("status") == "success":
        return data
      else:
        return {"error": data.get("message", "Unknown error")}
  except Exception as e:
    return {"error": str(e)}


def run_ip_lookup():
  print("\n" + "=" * 50)
  print(" IP Geolocation Lookup Utility")
  print("=" * 50)

  ip = input(
      "Enter target IP address (leave blank for your own IP): "
  ).strip()

  print(f"\n[*] Fetching geolocation data...")
  result = get_ip_location(ip)

  print("\n" + "=" * 50)
  if "error" in result:
    print(f"[-] Error: {result['error']}")
  else:
    print(f" Target IP    : {result.get('query')}")
    print(f" Country      : {result.get('country')} ({result.get('countryCode')})")
    print(f" Region/State : {result.get('regionName')}")
    print(f" City         : {result.get('city')}")
    print(f" ISP          : {result.get('isp')}")
    print(f" Organization : {result.get('org')}")
    print(f" Coordinates  : {result.get('lat')}, {result.get('lon')}")
  print("=" * 50 + "\n")


if __name__ == "__main__":
  run_ip_lookup()
