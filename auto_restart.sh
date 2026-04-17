#!/bin/bash

# =========================================================================
# Note: This script was used in Phase 1 to manually monitor and restart 
# the Python process using raw Linux commands. 
# This becomes obsolete as it is now 100% handled natively by 
# Docker Compose's 'restart: always' self-healing policy. 
# =========================================================================

# Define the script to check
SCRIPT_NAME="log_generator.py"

# Check if the process is running
# 'grep -v grep' removes the search command itself from the result
if ps aux | grep "$SCRIPT_NAME" | grep -v "grep" > /dev/null
then
    echo " System Status: $SCRIPT_NAME is running."
else
    echo " ALERT: $SCRIPT_NAME is STOPPED. Restarting now..."
    
    # Restart the script in the background
    nohup python3 /home/ec2-user/cloud-log-observability/log_generator.py &
    
    echo " Recovery Complete. Service restarted."
fi
