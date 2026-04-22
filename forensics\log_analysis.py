# Simple log parsing example

log_file = "access.log"

with open(log_file, "r") as file:
    for line in file:
        if "401" in line or "403" in line:
            print("Suspicious activity:", line.strip())
          
