# Cron Automation

Cron is Linux job scheduler.

crontab -e → edit cron jobs

---

## @reboot

@reboot /usr/bin/python3 /home/ec2-user/cloud_project/log_generator.py >> cron.log 2>&1

Runs once per system boot.

Important:
- Always use absolute paths
- Cron has limited environment
- Always redirect output

---

## Daily Rotation

0 0 * * * /home/ec2-user/cloud_project/log_rotate.sh >> cron_rotate.log 2>&1

Meaning:
Minute Hour Day Month Weekday
0      0     *    *      *

Runs every day at midnight.

---

## Output Redirection

>> file.log
Append output to file

2>&1
Redirect stderr to stdout

Cron runs silently, so logs are necessary for debugging.
