import getpass
import socket
import paramiko


def test_ssh_login(
    host: str,
    port: int,
    username: str,
    password: str,
    timeout: int = 5,
) -> tuple[bool, str]:
    """Test SSH connectivity and credential authentication against a remote host."""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(
            hostname=host,
            port=port,
            username=username,
            password=password,
            timeout=timeout,
            banner_timeout=timeout,
            auth_timeout=timeout,
            look_for_keys=False,
            allow_agent=False,
        )
        return True, f"Authentication successful on {host}:{port} as '{username}'."

    except paramiko.AuthenticationException:
        return False, f"Authentication failed on {host}:{port} — invalid username or password."

    except (socket.timeout, TimeoutError):
        return False, f"Connection timed out while reaching {host}:{port} (within {timeout}s)."

    except paramiko.SSHException as exc:
        return False, f"SSH error on {host}:{port}: {exc}"

    except OSError as exc:
        return False, f"Network/socket error reaching {host}:{port}: {exc}"

    finally:
        client.close()


def run_ssh_test() -> None:
    print("=" * 52)
    print(" SSH Login Test Utility")
    print("=" * 52)

    host_input = input("Enter target host/IP (default 127.0.0.1): ").strip()
    host = host_input if host_input else "127.0.0.1"

    port_input = input("Enter SSH port (default 22): ").strip()
    if not port_input:
        port = 22
    else:
        try:
            port = int(port_input)
            if not (1 <= port <= 65535):
                print("[!] Invalid port range. Using default port 22.")
                port = 22
        except ValueError:
            print("[!] Invalid port number. Using default port 22.")
            port = 22

    username = input("Enter SSH username: ").strip()
    password = getpass.getpass("Enter SSH password: ")

    print(f"\n[*] Testing SSH connection to {host}:{port}...")
    success, message = test_ssh_login(host, port, username, password)

    if success:
        print(f"[+] SUCCESS: {message}")
    else:
        print(f"[-] FAILED:  {message}")


if __name__ == "__main__":
    run_ssh_test()
