#!/bin/bash

# Define the script to check
SCRIPT_NAME="log_generator.py"

# Check if the process is running
# 'grep -v grep' removes the search command itself from the result
if ps aux | grep "$SCRIPT_NAME" | grep -v "grep" > /dev/null
then
    echo "✅ System Status: $SCRIPT_NAME is running."
else
    echo "🚨 ALERT: $SCRIPT_NAME is STOPPED. Restarting now..."
    
    # Restart the script in the background
    nohup python3 /home/ec2-user/cloud_project/log_generator.py &
    
    echo "♻️  Recovery Complete. Service restarted."
fi
