# Day 09: Show Command Execution

A Python-based network automation script that connects to a remote host or network device over SSH and executes a read-only/status command to retrieve its output.

## Features

- Connects over SSHv2 using `paramiko` with configurable host, port, username, and masked password input.
- Executes user-specified commands (defaulting to `uname -a`) and captures both `STDOUT` and `STDERR`.
- Handles authentication failures, timeouts, and network errors cleanly while closing the SSH session.

## Requirements

- Python 3.x
- External library: `paramiko` (`pip install paramiko`)
- Built-in libraries: `getpass`, `socket`

## How to Run

1. Install `paramiko` if not already installed:
   ```bash
   pip install paramiko
