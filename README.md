# Sage & Stone Kitchens (SUM Consumer)

Standalone Django/Wagtail project that consumes `sum-core`.

This repo is used as **Loop Site A** to validate deploy/upgrade/rollback workflows before production.

## Platform Pin

`requirements.txt` pins to:

- `sum-core @ v0.6.0` (public repo tag)

## Theme

This project includes a committed snapshot of Theme A under `theme/active/`.

Theme provenance is recorded in `.sum/theme.json`.

## Local Quick Start

```bash
cp .env.example .env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_sage_stone --clear
python manage.py runserver 8001
```

## Production Notes

- Production settings: `DJANGO_SETTINGS_MODULE=sage_and_stone.settings.production`
- Do not commit `.env` or any secrets.
