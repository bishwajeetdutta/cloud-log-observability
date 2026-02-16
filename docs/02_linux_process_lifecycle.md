# Linux Process Lifecycle

## 1. Foreground Process

python3 log_generator.py

- Stops when SSH closes
- Attached to terminal

---

## 2. Background Process

nohup python3 log_generator.py &

nohup:
- Prevents SIGHUP (hangup) signal
- Keeps process alive after logout

&:
- Runs process in background

---

## 3. SSH Disconnect vs Reboot

SSH disconnect:
- Only closes terminal session
- Does NOT stop system
- Does NOT trigger cron @reboot

sudo reboot:
- Restarts OS
- Restarts cron daemon
- Triggers @reboot entries

---

## 4. Process Identification

ps aux | grep log_generator.py

Find running process.

Kill process:
kill -9 <PID>

pkill -f log_generator.py
Kills process by matching name.

---

## 5. File Descriptors

Important Concept:

When a process opens a file:
- It gets a file descriptor
- It writes to that descriptor
- Not to the filename

Renaming file does NOT change descriptor.

This is why log rotation requires restart.
