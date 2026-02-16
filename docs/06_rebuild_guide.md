# Rebuild Guide (From Scratch)

If EC2 is deleted:

1. Launch new EC2 (Amazon Linux)
2. Install Git:
   sudo yum install git -y

3. Clone repo:
   git clone git@github.com:USERNAME/cloud-log-observability.git

4. Install Python if needed

5. Apply cron:
   crontab crontab_backup.txt

6. Verify:
   ps aux | grep log_generator.py
   tail -f server.log

System restored.
