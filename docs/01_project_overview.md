# Cloud Log Observability - Phase 1 (Linux Automation Layer)

## Project Goal
Build a self-managing log generation system on EC2 that:

- Continuously generates logs
- Survives SSH logout
- Survives system reboot
- Rotates logs daily
- Deletes logs older than 7 days
- Automatically restarts service after rotation

This phase focuses purely on Linux process lifecycle and automation.
No Docker. No managed cloud services.

---

## Components

1. log_generator.py
   - Continuously writes logs to server.log
   - Uses Python logging module

2. log_monitor.py
   - Tails log file in real-time
   - Detects ERROR entries

3. auto_restart.sh
   - Checks if generator is running
   - Restarts if stopped

4. log_rotate.sh
   - Renames log file with timestamp
   - Creates fresh log
   - Restarts generator
   - Deletes old logs (>7 days)

5. Cron
   - @reboot for persistence
   - Midnight schedule for rotation

---

## System Behavior Summary

Boot → Cron runs generator  
Generator writes logs  
At midnight → rotate logs  
Rotation → restart generator  
Delete logs older than 7 days  
System runs without human intervention
