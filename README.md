
### Run

#### Change .env

```bash
docker compose up --build
```

```bash
alembic upgrade head
```

```bash
 uvicorn src.main:app --port 8000 --reload

```