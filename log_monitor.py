import time

# UPDATE THIS LINE TO THE ABSOLUTE PATH
LOG_FILE = "server.log"

def follow(file):
    file.seek(0, 2)  # Move to the end of the file
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line

try:
    with open(LOG_FILE, "r") as f:
        loglines = follow(f)
        for line in loglines:
            if "ERROR" in line:
                print("ALERT! ⚠️ ERROR detected ->", line.strip())
            else:
                print("OK:", line.strip())
except FileNotFoundError:
    print(f"Error: Could not find log file at {LOG_FILE}. Is the generator running?")
