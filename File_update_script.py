# Python Script: Update Allow List by Removing IPs from Remove List
# Author: Tinashe Zacariah
# Description: This script removes IP addresses from an allow list file based on a remove list.

# Define the file to update
import_file = "allow_list.txt"

# Sample remove list (could be sourced externally)
remove_list = ["192.168.0.105", "10.0.0.25"]

# Step 1: Open the file and read contents
with open(import_file, "r") as file:
    ip_addresses = file.read()

# Step 2: Convert string to list
ip_addresses = ip_addresses.split()

# Step 3: Remove any IP addresses in remove_list from ip_addresses
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Step 4: Convert the updated list back to string format
updated_ips = "\n".join(ip_addresses)

# Step 5: Write the updated IPs back to the file
with open(import_file, "w") as file:
    file.write(updated_ips)

print("Allow list updated successfully.")
