
# 1. Use a lightweight Python Linux (Alpine is tiny)
FROM python:3.9-slim

# 2. Create a folder inside the container
WORKDIR /app

# 3. Copy files from Host (EC2) to Container (/app)
COPY log_generator.py  .
COPY log_monitor.py .

# 4. The command to run when the container starts
CMD ["python", "log_generator.py"]
