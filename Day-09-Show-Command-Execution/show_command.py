import getpass
import socket
import paramiko


def execute_show_command(
    host: str,
    port: int,
    username: str,
    password: str,
    command: str,
    timeout: int = 5,
) -> tuple[bool, str, str]:
    """Connect via SSH, run a command, and return (connected, stdout_text, stderr_text)."""
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

        _, stdout, stderr = client.exec_command(command, timeout=timeout)
        out_text = stdout.read().decode("utf-8", errors="replace").strip()
        err_text = stderr.read().decode("utf-8", errors="replace").strip()
        return True, out_text, err_text

    except paramiko.AuthenticationException:
        return False, "", "Authentication failed — invalid username or password."

    except (socket.timeout, TimeoutError):
        return False, "", f"Connection or command timed out after {timeout}s."

    except paramiko.SSHException as exc:
        return False, "", f"SSH error: {exc}"

    except OSError as exc:
        return False, "", f"Network/socket error: {exc}"

    finally:
        client.close()


def run_show_command() -> None:
    print("=" * 56)
    print(" Show Command Execution Utility (SSH)")
    print("=" * 56)

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

    cmd_input = input("Enter command to run (default 'uname -a'): ").strip()
    command = cmd_input if cmd_input else "uname -a"

    print(f"\n[*] Connecting to {host}:{port} and running: {command}\n")
    connected, out_text, err_text = execute_show_command(
        host=host,
        port=port,
        username=username,
        password=password,
        command=command,
    )

    if not connected:
        print(f"[-] FAILED: {err_text}")
        return

    print("-" * 56)
    print(" Command Output (STDOUT):")
    print("-" * 56)
    print(out_text if out_text else "[No standard output returned]")

    if err_text:
        print("-" * 56)
        print(" Error Output (STDERR):")
        print("-" * 56)
        print(err_text)

    print("-" * 56)


if __name__ == "__main__":
    run_show_command()
