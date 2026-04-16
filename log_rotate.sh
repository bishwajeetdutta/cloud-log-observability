#!/bin/bash

LOG_DIR="/home/ec2-user/cloud-log-observability"
LOG_FILE="$LOG_DIR/server.log"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="$LOG_DIR/server.log.$TIMESTAMP"

if [ -f "$LOG_FILE" ]; then
    # 1. Rotate the current log
    sudo mv "$LOG_FILE" "$BACKUP_FILE"
    
    # 2. Create a fresh empty log file
    sudo touch "$LOG_FILE"
    
    # 3. Restart the Generator (Crucial for Inode release)
    #pkill -f log_generator.py
    #nohup python3 /home/ec2-user/cloud_project/log_generator.py > /dev/null 2>&1 &
    sudo docker restart compose-generator

    # 4. Cleanup (Retention Policy: Delete logs older than 7 days)
    # Uses [0-9]* to only match timestamped files, not other .log files
    sudo find "$LOG_DIR" -name "server.log.[0-9]*" -mtime +7 -delete
    
    echo "✅ Log rotated: $BACKUP_FILE created. Old logs (>7 days) deleted."
else
    echo "⚠️  No log file found."
fi
