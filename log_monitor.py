import time
import os
import boto3
from datetime import datetime

LOG_FILE = "server.log"
BUCKET_NAME = "cloud-log-analyzer-errors"

print("Starting Log Monitor with AWS S3 Uplink...")

# Initialize the S3 client (It automatically uses the IAM role we attached!)
s3 = boto3.client('s3', region_name='ap-south-1')

# Create a blank file if it doesn't exist yet to prevent crashes
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
            print(f"ALERT! ⚠️ ERROR detected -> {line.strip()}")
            
            # 1. Create a unique filename based on the current timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            error_filename = f"error_log_{timestamp}.txt"
            
            # 2. Save the error to a temporary file inside the container
            with open(error_filename, "w") as error_file:
                error_file.write(line)
            
            # 3. Upload that file to your S3 Bucket
            try:
                s3.upload_file(error_filename, BUCKET_NAME, error_filename)
                print(f"✅ Successfully uploaded {error_filename} to S3!")
            except Exception as e:
                print(f"❌ Failed to upload to S3: {e}")
