# Quiz

A general-knowledge quiz app built with Flask and SQLite. Pick a category, answer against the clock-free round, get a scored result.

## Stack

- Flask 3 (app factory + blueprint)
- Flask-SQLAlchemy (SQLite by default, swap in Postgres via `DATABASE_URL`)
- Server-side sessions for per-player state (no shared global state — safe for concurrent players)
- Vanilla HTML/CSS, no JS framework, Space Grotesk + Inter

## Local setup

```
git clone https://github.com/ScyrolynX/QUIZ.git
cd QUIZ
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python seed.py
python wsgi.py
```

App runs at `http://localhost:5000`.

## Project structure

```
app/
  __init__.py     # app factory
  models.py       # Question model
  routes.py       # blueprint: home, start, question, result
  templates/
config.py         # env-driven config
seed.py           # seeds the question bank
wsgi.py           # entrypoint for gunicorn
```

## Deploying

Works on any platform that runs a `Procfile` (Render, Railway, Fly.io):

```
web: gunicorn wsgi:app
```

Set `SECRET_KEY` and `DATABASE_URL` as environment variables in your host's dashboard — never commit `.env`.

## Adding questions

Add rows via `seed.py`, or insert directly through the `Question` model — no code changes needed elsewhere.
