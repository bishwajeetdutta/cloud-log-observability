import time
import os
import boto3
from datetime import datetime

LOG_FILE = "/app/server.log"
BUCKET_NAME = "cloud-log-analyzer-errors"
ERROR_DIR = "/app/errors"

print("Starting Log Monitor with AWS S3 Uplink...")

os.makedirs(ERROR_DIR, exist_ok=True)

s3 = boto3.client('s3', region_name='ap-south-1')

if not os.path.exists(LOG_FILE):
    open(LOG_FILE, 'w').close()

with open(LOG_FILE, "r") as f:
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if not line:
            time.sleep(1)
            continue

        if "ERROR" in line:
            print(f"ALERT! ERROR detected -> {line.strip()}")

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            error_filename = f"error_log_{timestamp}.txt"
            error_filepath = f"{ERROR_DIR}/{error_filename}"

            with open(error_filepath, "w") as error_file:
                error_file.write(line)

            try:
                s3.upload_file(error_filepath, BUCKET_NAME, error_filename)
                print(f"Uploaded {error_filename} to S3!")
                os.remove(error_filepath)
                print(f"Deleted local file {error_filename}")
            except Exception as e:
                print(f"Failed to upload to S3: {e}")

