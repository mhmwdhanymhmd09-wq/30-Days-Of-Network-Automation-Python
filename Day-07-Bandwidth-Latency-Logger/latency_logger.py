import subprocess
import platform
import time
import datetime

def ping_host(host="8.8.8.8"):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    
    start_time = time.time()
    result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    end_time = time.time()
    
    if result.returncode == 0:
        latency = round((end_time - start_time) * 1000, 2)
        return latency
    else:
        return None

def run_logger():
    print("=" * 50)
    print(" Bandwidth & Latency Logger Utility")
    print("=" * 50)
    
    target = input("Enter target host/IP to monitor (default 8.8.8.8): ").strip()
    if not target:
        target = "8.8.8.8"
        
    print(f"\n[*] Logging latency for {target}. Press Ctrl+C to stop.\n")
    print(f"{'Timestamp':<22} | {'Target':<15} | {'Status / Latency'}")
    print("-" * 55)
    
    try:
        while True:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            latency = ping_host(target)
            
            if latency is not None:
                status = f"Connected ({latency} ms)"
            else:
                status = "Request Timed Out / Failed"
                
            print(f"{timestamp:<22} | {target:<15} | {status}")
            time.sleep(2)
            
    except KeyboardInterrupt:
        print("\n\n[*] Monitoring stopped by user. Logger exiting safely.")

if __name__ == "__main__":
    run_logger()
