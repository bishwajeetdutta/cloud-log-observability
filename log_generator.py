import logging
import time
import random
import os

# Setup logging to write to a file
logging.basicConfig(
    #filename='server.log', # did this for docker phase to see the logs on screen and do not have to get inside the fake-server to see the logs
    filename='server.log', # <---Add this back
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

pid = os.getpid()
print(f"Server Started! Running with PID: {pid}")

while True:
    # Simulate traffic
    if random.randint(1, 10) <= 8:
        logging.info(f"Health Check OK. Process {pid} running.")
    else:
        logging.error("DB Connection Failed! Timeout.")

    # Sleep for 3 seconds so we don't fill the disk too fast
    time.sleep(3)
