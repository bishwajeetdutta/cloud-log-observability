# Common Problems

## SSH Broken Pipe
Not reboot.
Just network disconnect.

---

## Cron Not Running
Check:
crontab -l
Check log file:
cron.log

---

## Rotation Not Working
Check:
cron_rotate.log

---

## Logs Writing to Backup File
Cause:
File descriptor still open.

Fix:
Restart application after rotation.

---

## Git Push Permission Denied
Cause:
SSH key not added to GitHub.

Fix:
Generate ssh key
Add to GitHub settings
