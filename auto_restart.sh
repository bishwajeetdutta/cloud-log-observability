#!/bin/bash

#not useful anymore


SCRIPT_NAME="log_generator.py"

# Check if process is running
if ps aux | grep "$SCRIPT_NAME" | grep -v "grep" > /dev/null
then
    echo " System Status: $SCRIPT_NAME is running."
else
    echo " ALERT: $SCRIPT_NAME is STOPPED. Restarting now..."
    
    # Restart the script in the bg
    nohup python3 /home/ec2-user/cloud-log-observability/log_generator.py &
    
    echo " Recovery Complete. Service restarted."
fi


