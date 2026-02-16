# EC2 Setup Steps

sudo yum update -y
sudo yum install docker -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ec2-user

# Apply cron
crontab crontab_backup.txt

