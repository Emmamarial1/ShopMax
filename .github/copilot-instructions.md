## Quick orientation — ShopMax (Flask monolith)

This repository is a single-process Flask application (development SQLite) with most routing and models defined in `app.py` (there's also a `models.py` file with duplicated model shapes). Key app behavior and helper scripts live in the repository root.

Keep these facts top-of-mind when suggesting edits or producing code:

- App entry: `app.py` — it both defines models and routes and is the canonical server entrypoint (runs `app.run(debug=True)`).
- Local DB: SQLite files live in the project root (`shopmax.db`, `users.db`).
- Migrations: `migrations/` is configured (Flask-Migrate / Alembic). Migration scripts are in `migrations/versions/*.py`.
- Dev utilities: use the scripts in the root for common tasks — `recreate_database.py`, `remove_tracking_fix.py`, `verify_fix.py`, `check_models.py`, `final_check.py`, `test_users.py`, `backup_users.py`.

Useful commands (Windows PowerShell):

```
# start development server
python app.py

# use Flask-Migrate (set env var before running flask commands in PowerShell)
$env:FLASK_APP = 'app.py'
$env:FLASK_ENV = 'development'
flask db migrate -m "message"
flask db upgrade

# quick helpers
python recreate_database.py    # deletes SQL file and re-creates tables + sample data
python remove_tracking_fix.py  # resets DB to a simpler order model if migrations break
python verify_fix.py           # sanity-check order table / columns
python check_models.py         # compare SQL table columns to model attributes
python test_users.py           # creates sample users in DB
python backup_users.py         # dumps users to user_backup.json
```

Repository-specific patterns and gotchas
- Models are defined twice: `app.py` contains full models (and helper functions). `models.py` has a largely overlapping definition. When editing models, update the location that scripts/other modules import from — some scripts import from `models.py`, some from `app.py`.
- Many helper scripts run in an app context (they import `app` and `db` and call `db.create_all()` or query models). Always run them from the repository root so relative DB paths resolve correctly.
- SQLite is the default development DB — migrations + production DBs may differ. Prefer running `flask db` commands when adjusting schema; fallback to the helper scripts only if migrations are broken.
- Email + uploads: SMTP config is in `app.py` and file uploads are saved to `static/uploads` using `UPLOAD_FOLDER`. Secrets are sometimes hard-coded; treat these as dev-only and check for environment variables before editing.

Where to look for examples
- Authentication & user model: `app.py` (search for `User`) — user_type is `buyer|seller|admin` and drives many flows.
- Migration examples: `migrations/versions/3bce909cae65_initial...py` and `d048ccc0c6b8_add_google_oauth_fields.py` show how schema changes are done in this repo.
- DB reset + verification patterns: `recreate_database.py`, `remove_tracking_fix.py`, `verify_fix.py`, `check_models.py`.

When proposing changes
- Use the existing migration system, update `migrations/` and add a migration via `flask db migrate` + `flask db upgrade` rather than editing `shopmax.db` directly.
- If your change touches models that scripts import from `models.py` vs `app.py`, keep both files in sync or update imports so there's a single source of truth.
- Keep production-sensitive values (secrets, SMTP passwords) in environment variables or config files. Don’t hard-code credentials in changes.

If anything here is unclear or you'd like this tuned toward tests / CI workflows, tell me what workflows you want covered and I’ll iterate.
