# Setup Notes

This file contains notes I kept while setting up this project on AWS EC2.

## AWS IAM Role Setup

1. Go to AWS Console -> IAM -> Roles -> Create Role
2. Trusted entity: AWS Service → EC2
3. Attach policy: `AmazonS3FullAccess`
4. Name it: `ec2-s3-log-role`
5. Modify IAM role.

## S3 Bucket Setup

1. Create a bucket named `cloud-log-analyzer-errors` in `ap-south-1`
2. Keep "Block all public access" ON
3. Life Cycle rule is created to expire objects after 7 days.

## AWS EC2

1. Launch an EC2 instance (Amazon Linux)
2. Open these ports in your EC2 Security Group:
- Port 22 (SSH) - your IP only
- Port 3000 (Grafana) - Anywhere IPv4


## Setup

```bash

# Install git
sudo dnf update -y
sudo dnf install git -y

# Install Docker
sudo yum update -y
sudo yum install docker -y
sudo service docker start
sudo systemctl enable docker
sudo usermod -a -G docker ec2-user

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
## Deployment
```bash
git clone https://github.com/bishwajeetdutta/cloud-log-observability.git
cd cloud-log-observability
docker compose up -d --build
```

## Grafana Setup

1. Access at `http://YOUR-EC2-IP:3000`
2. Login: admin / admin
3. Add PostgreSQL as data source:
   - Host: `postgres:5432`
   - Database: `logsdb`
   - User: `loguser`
   - Password: `logpassword`
   - SSL Mode: disable
4. Create a new dashboard -> Add panel -> Use this query:

```sql
SELECT
  $__timeGroupAlias(timestamp, $--interval),
  error_type AS metric,
  count(id) AS "Error Count"
FROM error_logs
WHERE $__timeFilter(timestamp)
GROUP BY 1, 3
ORDER BY 1
```


