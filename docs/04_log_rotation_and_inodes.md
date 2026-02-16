# Log Rotation and Inode Behavior

## Rotation Logic

1. Rename current log
2. Create new empty log
3. Restart application
4. Delete old logs

---

## Why Restart is Required

Process holds file descriptor.

After:

mv server.log server.log.timestamp

Process still writes to old file descriptor.

New server.log is ignored.

Solution:
Restart process so it reopens new file.

---

## log_rotate.sh Steps

1. mv server.log → server.log.TIMESTAMP
2. touch server.log
3. pkill log_generator.py
4. nohup restart
5. find delete old logs
