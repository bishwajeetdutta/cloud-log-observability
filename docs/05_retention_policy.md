# Log Retention Policy

Goal:
Prevent disk from filling.

Command used:

find "$LOG_DIR" -name "server.log.[0-9]*" -mtime +7 -delete

Meaning:

-name "server.log.[0-9]*"
Match rotated logs only

-mtime +7
Older than 7 full 24-hour periods

-delete
Remove file permanently

---

Retention ensures:

- Disk usage stays controlled
- Old logs are automatically cleaned
- System runs indefinitely
