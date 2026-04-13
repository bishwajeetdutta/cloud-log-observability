# Phase 1.5 — Docker Basics

## Why Docker Was Introduced

In Phase 1, the system relied on:

- nohup for background execution
- cron @reboot for persistence
- manual restart scripts
- host-level Python installation

This created operational complexity:
- Process management was manual
- Environment consistency was not guaranteed
- Rebuilding on new EC2 required reinstalling everything

Docker is introduced to solve:

- Environment portability
- Process isolation
- Built-in restart policies
- Reproducible infrastructure


------------------------------------------------------------

## What is Docker?

Docker is a containerization platform.

It allows applications to run inside lightweight, isolated environments called containers.

A container includes:
- Application code
- Runtime (Python)
- Dependencies
- System libraries

Everything needed to run the application.


------------------------------------------------------------

## Key Concepts

### 1. Image

An image is a blueprint.

It contains:
- Base OS (e.g., python:3.9-slim)
- Application code
- Installed dependencies
- Startup command

Images are built using a Dockerfile.

Images are read-only templates.


### 2. Container

A container is a running instance of an image.

If image = blueprint,
container = running machine created from that blueprint.

Multiple containers can be created from the same image.


### 3. Dockerfile

A Dockerfile defines how to build an image.

It contains instructions like:

- FROM
- WORKDIR
- COPY
- RUN
- CMD

Example structure:

FROM python:3.9-slim
WORKDIR /app
COPY log_generator.py .
CMD ["python", "log_generator.py"]


### 4. Docker Daemon

Docker runs as a background service on the host machine.

It:
- Builds images
- Runs containers
- Manages container lifecycle


------------------------------------------------------------

## Core Docker Commands Used

### Build an Image

docker build -t log-generator .

- -t assigns a tag (name)
- . means current directory contains Dockerfile


### Run a Container

docker run -d --name generator log-generator

- -d runs in detached mode
- --name assigns container name
- log-generator is image name


### List Running Containers

docker ps


### Stop a Container

docker stop generator


### Remove a Container

docker rm generator


### View Container Logs

docker logs generator


------------------------------------------------------------

## How Docker Replaces Phase 1 Components

| Phase 1 Tool          | Docker Replacement       |
|-----------------------|--------------------------|
| nohup                 | docker run -d            |
| cron @reboot          | --restart unless-stopped |
| manual restart script | restart policy           |
| host python install   | image-contained python   |


------------------------------------------------------------

## Restart Policies

Docker provides built-in restart mechanisms.

Example:

docker run -d \
  --name generator \
  --restart unless-stopped \
  log-generator

Restart policies:

- no (default)
- on-failure
- always
- unless-stopped

This replaces cron-based reboot logic.


------------------------------------------------------------

## Container Isolation

Containers are isolated from the host system:

- Separate filesystem
- Separate process namespace
- Separate network stack (by default)

This means:

Files created inside container are NOT visible on host
unless volumes are used.


------------------------------------------------------------

## Volumes (Preview for Next Step)

A volume allows:

Host directory <--> Container directory mapping

Example:

docker run -d \
  -v /home/ec2-user/cloud_project:/app/logs \
  log-generator

This allows:

- Logs generated inside container
- Visible on EC2 host
- Accessible to monitor script


------------------------------------------------------------

## Important Engineering Lessons

1. Containers are not virtual machines.
2. Containers are lightweight and share host kernel.
3. Restart policies eliminate need for cron-based persistence.
4. Images make infrastructure reproducible.
5. Docker simplifies rebuilding on new EC2 instance.


------------------------------------------------------------

## Architectural Shift from Phase 1 to Phase 1.5

Phase 1:
Host-managed process lifecycle.

Phase 1.5:
Container-managed process lifecycle.

This moves responsibility from:
Manual Linux scripting → Platform-level orchestration.


------------------------------------------------------------

## Why Docker Matters for Cloud Engineering

- Standardized deployments
- CI/CD compatibility
- Multi-environment portability
- Scalable microservice architecture
- Production-level infrastructure design

Docker is foundational for:
- Kubernetes
- ECS
- DevOps pipelines
- Modern cloud systems
