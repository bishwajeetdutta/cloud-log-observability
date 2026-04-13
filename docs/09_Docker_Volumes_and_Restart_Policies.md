# 1. Docker Volume

Containers are ephemeral (temporary). If your server reboots or the container crashes, Docker destroys the container and builds a brand new one from the image. Any logs or data saved inside the old container are wiped from existence.

By default, when a container dies, everything inside it dies.  
Never store important data (like databases or logs) purely inside a container.

---

## The `-v` (Volume) Flag

```bash
docker run -d --name fake-server -v /home/ec2-user/cloud_project:/app log-generator
```

### Translation:

Run the container in the background.  
Take the `/home/ec2-user/cloud_project` folder on my EC2, and glue it to the `/app` folder inside the container.

---

### What This Means Practically

The container may think it is writing to:

```
/app/server.log
```

But because of the volume mapping:

```
/home/ec2-user/cloud_project  <---->  /app
```

The file is actually being written directly onto your EC2 hard drive.

So even if the container dies, the data survives.

This is how we persist logs and databases safely.

---

# 2. Restart Policies

In Phase 1, we worked hard to make the script survive crashes and reboots.

We had to:
- Write an `auto_restart.sh` script
- Configure `crontab`
- Use `@reboot`
- Manually monitor processes

Docker replaces all of that hard work with one single word.

Docker has a built-in "heartbeat monitor."

Instead of writing custom bash scripts or cron jobs to revive dead processes, you just tell Docker what to do if the container stops or the server reboots.

---

## `--restart always`

This tells the Docker Daemon:

"If this container dies, or if the EC2 server reboots, bring it back to life immediately."

---

## Example Command

```bash
docker run -d --name fake-server --restart always -v /home/ec2-user/cloud_project:/app log-generator
```

Now:

- If the container crashes → Docker restarts it.
- If the EC2 reboots → Docker restarts it.
- No cron.
- No custom restart script.
- No manual intervention.

---

## Architectural Shift

Phase 1:
Linux-managed lifecycle (cron + bash scripts)

Phase 1.5:
Docker-managed lifecycle (restart policies)

This reduces complexity and improves reliability.
