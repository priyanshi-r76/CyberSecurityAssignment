# Cyber Safety Toolkit

import os
import shutil

print("=== Cyber Safety Toolkit ===")

print("1. Password Strength Checker")
print("2. File Backup Tool")
print("3. File Permission Checker")

choice = input("Enter your choice: ")

# Password Strength Checker
if choice == "1":

    password = input("Enter password: ")

    if len(password) >= 8:
        print("Strong Password")

    else:
        print("Weak Password")

# File Backup Tool
elif choice == "2":

    source = input("Enter source file name: ")

    backup = source + ".backup"

    shutil.copy(source, backup)

    print("Backup created successfully")

# File Permission Checker
elif choice == "3":

    file = input("Enter file name: ")

    permissions = oct(os.stat(file).st_mode)[-3:]

    print("File Permissions:", permissions)

else:
    print("Invalid Choice")
