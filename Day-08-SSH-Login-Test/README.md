# Day 08: SSH Login Test

A Python-based network automation utility designed to test SSH connectivity and credential authentication against network devices or remote hosts.

## Features

- Tests real SSHv2 connections to a specified host/IP and port (default `22`).
- Masks password input in the terminal using `getpass`.
- Separates authentication errors, timeouts, and network/SSH errors with clear status messages.
- Closes SSH sessions cleanly after each test.

## Requirements

- Python 3.x
- External library: `paramiko` (`pip install paramiko`)
- Built-in libraries: `getpass`, `socket`

## How to Run

1. Install `paramiko` if not already installed:
   ```bash
   pip install paramiko
