import logging
import time
import random
import os

# writing logs to a file inside the container
logging.basicConfig(
    filename='/app/server.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

pid = os.getpid()
print(f"Server Started! Running with PID: {pid}")

while True:
    # 80% chance of INFO, 20% chance of ERROR
    if random.randint(1, 10) <= 8:
        logging.info(f"Health Check OK. Process {pid} running.")
    else:
        logging.error("DB Connection Failed! Timeout.")

    # wait 3 seconds so we dont fill disk too fast
    time.sleep(3)
