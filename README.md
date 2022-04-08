## Installation

Build & Launch

```bash
docker-compose up --build
```

To shut down:

```bash
docker-compose down
```

To run in daemon mode:
```bash
docker-compose up -d --build
```

## Usages

Home
http://127.0.0.1:5001/

Count tweets
http://127.0.0.1:5001/count

Result of the task
http://127.0.0.1:5001/check/<task_id>

Monitor tasks
http://127.0.0.1:5555/
