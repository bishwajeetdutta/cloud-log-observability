#!/bin/bash

LOG_DIR="/home/ec2-user/cloud-log-observability"
ARCHIVE_DIR="$LOG_DIR/archives"
LOG_FILE="$LOG_DIR/server.log"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="$ARCHIVE_DIR/server.log.$TIMESTAMP"

sudo mkdir -p "$ARCHIVE_DIR"

if [ -f "$LOG_FILE" ]; then
    # move the current log to archives folde
    sudo mv "$LOG_FILE" "$BACKUP_FILE"

    # create a fresh empty log file for new logs to go into
    sudo touch "$LOG_FILE"

    # restart the containers so they start writing to the new log file so that old files close and logs go into the right place
    sudo docker restart compose-generator compose-monitor

    # delete archived logs more than 7 days old
    sudo find "$ARCHIVE_DIR" -name "server.log.[0-9]*" -mtime +7 -delete

    echo "Log rotated successfully. Old archives cleaned up."
else
    echo "No log file found at $LOG_FILE"
fi
