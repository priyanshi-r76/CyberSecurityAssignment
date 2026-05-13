# Cyber Network Detective

import socket
import os

print("=== Cyber Network Detective ===")
print("1. Ping Scanner")
print("2. DNS Lookup Tool")
print("3. IP Address Information")
choice = input("Enter your choice: ")

# Ping Scanner
if choice == "1":
    host = input("Enter website or IP address: ")
    response = os.system("ping -c 1 " + host)
    if response == 0:
        print("Host is Active")
    else:
        print("Host is Not Reachable")

# DNS Lookup
elif choice == "2":
    domain = input("Enter domain name: ")
    ip = socket.gethostbyname(domain)
    print("IP Address:", ip)

# IP Information
elif choice == "3":
    ip = input("Enter IP address: ")
    parts = ip.split(".")
    print("IP Parts:", parts)
    print("IP Version: IPv4")
else:
    print("Invalid Choice")
