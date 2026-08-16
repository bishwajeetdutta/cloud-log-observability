import time
import os
import boto3
import psycopg2
from datetime import datetime

LOG_FILE = "/app/server.log"
BUCKET_NAME = "cloud-log-analyzer-errors"
ERROR_DIR = "/app/errors"

print("Starting Log Monitor..watching for errors")

#make sure errors folder exist
os.makedirs(ERROR_DIR, exist_ok=True)

# Connect to s3
s3 = boto3.client('s3', region_name='ap-south-1')

# connect to postgreSQL
def connect_db():
    while True:
	#Might take time to start..cause its heavy
        try:
            conn = psycopg2.connect(
                host="postgres",
                database="logsdb",
                user="loguser",
                password="logpassword"
            )
            print("Connected to PostgreSQL!")
            return conn
        except Exception as e:
            print(f"PostgreSQL not ready yet {e}")
            time.sleep(5) #try again

# Create table if it doesn't exist
def setup_db(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS error_logs (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP,
            error_type VARCHAR(100),
            message TEXT
        )
    """)
    conn.commit()
    cursor.close()
    print("Database table ready!")

# Insert error into PostgreSQL
# Instead of using f-strings, used %s to avoid SQL injection
def insert_error(conn, timestamp, error_type, message):
    try:
        cursor = conn.cursor()
        sql = """INSERT INTO error_logs 
                 (timestamp, error_type, message) 
                 VALUES (%s, %s, %s)"""
        data = (timestamp, error_type, message)
        cursor.execute(sql, data)
        conn.commit()
        cursor.close()
        print(f"Saved to database")
    except Exception as e:
        print(f"Couldn't save to database: {e}")

# Connect to DB
conn = connect_db()
setup_db(conn)

# Create log file if it doesn't exist
if not os.path.exists(LOG_FILE):
    open(LOG_FILE, 'w').close()

#start watching the log files from the end
with open(LOG_FILE, "r") as f:
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if not line:
            time.sleep(1)
            continue

        if "ERROR" in line:
            print(f"ERROR detected -> {line.strip()}")

            timestamp = datetime.now()
            error_type = "DB Connection Failed"
            error_filename = f"error_log_{timestamp.strftime('%Y%m%d_%H%M%S')}.txt"
            error_filepath = f"{ERROR_DIR}/{error_filename}"

            # Save error file locally(temp files)
            with open(error_filepath, "w") as error_file:
                error_file.write(line)

            #Upload to S3 and delete the local copy
            try:
                s3.upload_file(error_filepath, BUCKET_NAME, error_filename)
                os.remove(error_filepath)
            except Exception as e:
                print(f"Failed to upload to S3: {e}")

            # also save to database
            insert_error(conn, timestamp, error_type, line.strip())
