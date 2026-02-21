# 1. What is Docker Compose?

Docker Compose is a tool that lets you define and run multi-container applications using a YAML file.

You write one file:

```yaml
version: "3.9"

services:
  app:
    build: .
    ports:
      - "8000:8000"

  db:
    image: postgres
    restart: unless-stopped
```

Then run:

```bash
docker compose up -d
```

And boom 💥  
Whole environment is created automatically.

This is Infrastructure as Code because your infrastructure is written in a file.  
It is reproducible and anyone can clone it.

Instead of remembering 8 commands, you commit:

`docker-compose.yml`

Now entire infrastructure becomes portable, shareable and deployable.

---

# 2. YAML

YAML is:

- Indentation based  
- Uses spaces (NOT tabs)  
- Extremely sensitive to alignment  

If spacing is wrong → it breaks.

## Basic Structure

```yaml
key: value

name: Bishwa
role: Cloud Engineer
```

---

## docker run vs docker compose

| docker run           | docker compose                    |
| -------------------- | --------------------------------- |
| Manual               | Automated                         |
| Hard to reproduce    | Fully reproducible                |
| Not scalable         | Designed for multi-container apps |
| Easy to forget flags | All defined in file               |
