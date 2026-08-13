# Cloud-Native Log Observability & Analytics

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![AWS S3](https://img.shields.io/badge/AWS_S3-569A31?style=for-the-badge&logo=amazon-s3&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Overview
A production-grade, cloud-native log monitoring system built on AWS EC2 that automatically generates, detects, stores, and visualizes server logs in real-time. This project mimics enterprise-level data architecture, transitioning raw system text into actionable visual dashboards.

## System Architecture

```mermaid
graph TD
    A[Log Generator Container] -->|Writes| B(server.log)
    C[Log Monitor Container] -->|Tails & Parses| B
    C -->|Cold Storage Backup| D[AWS S3 Bucket]
    C -->|Hot Storage Insert| E[(PostgreSQL Container)]
    F[Grafana Dashboard] -->|Queries| E
```

## Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python** | Log generation + monitoring |
| **Bash & Cron** | Linux automation scripts |
| **Docker Compose** | Containerization + orchestration |
| **AWS EC2** | Cloud compute server |
| **AWS S3** | Error log backup (cold storage) |
| **AWS IAM** | Secure role-based access |
| **PostgreSQL** | Structured log storage (hot storage) |
| **Grafana** | Real-time visualization dashboard |

## How It Works (The Pipeline)

### 1. Linux Automation & Generation
* `log_generator.py` simulates a live production server by generating traffic and intermittent errors.
* Automated via Bash (`auto_restart.sh`) and Linux Cron to survive server reboots and manage log rotation to prevent storage overflow.

### 2. Dual-Storage Routing
* A Python watchdog tails the live server logs to detect critical ERROR states.
* **Cold Storage (Disaster Recovery):** Boto3 authenticates automatically via IAM roles (zero hardcoded credentials) to bundle and upload raw error files to **AWS S3**.
* **Hot Storage (Analytics):** Parses log strings and securely inserts them into **PostgreSQL** using parameterized queries to prevent SQL injection.

### 3. Container Orchestration & Visualization
* The entire environment is containerized using Docker Compose for seamless networking and self-healing (`restart: always` policies).
* **Grafana** connects directly to the PostgreSQL container via the private Docker network. Time-series queries group errors by minute to populate a live visualization dashboard.

