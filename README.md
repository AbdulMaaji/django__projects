# RiffMates (Django project)

Small Django demo project used while developing the RiffMates site and a tiny todo app.

## Quick overview
- Django 5.2.x (installed in the project's virtual environment `.venv`).
- SQLite DB at `db.sqlite3` (development only).
- `home` app contains simple pages and a small React prototype injected into `base.html`.
- `todo` app contains a minimal to-do list.

## Important templates / routes
- `/news/` → renders the original list-style news page (template: `home/templates/news/news2.html`).
- `/news-test/` → renders the React-styled test page (template: `home/templates/news_test.html`).

> Note: A malformed `home/templates/news2.html` template was removed to avoid TemplateSyntaxError. Use `news_test.html` for the React demo.

## Setup (Windows / PowerShell)
From the project root (`C:\Users\USER\Desktop\RiffMates`):

1. Activate the virtual environment (created at `.venv`):

```powershell
C:\Users\USER\Desktop\RiffMates\.venv\Scripts\Activate.ps1
```

2. (Optional) Install dependencies if you don't have them:

```powershell
C:\Users\USER\Desktop\RiffMates\.venv\Scripts\python.exe -m pip install -r requirements.txt
# If requirements.txt doesn't exist: pip install django
```

3. Apply migrations (creates/updates `db.sqlite3`):

```powershell
C:\Users\USER\Desktop\RiffMates\.venv\Scripts\python.exe manage.py makemigrations
C:\Users\USER\Desktop\RiffMates\.venv\Scripts\python.exe manage.py migrate
```

4. Run the development server:

```powershell
C:\Users\USER\Desktop\RiffMates\.venv\Scripts\python.exe manage.py runserver
```

Open http://127.0.0.1:8000/news/ and http://127.0.0.1:8000/news-test/ in your browser.

## Notes & troubleshooting
- If Django raises a `DisallowedHost` during automated tests or test client requests, add `testserver`, `localhost`, or `127.0.0.1` to `ALLOWED_HOSTS` in `RiffMates/settings.py` for convenience while testing.
- The React widget is included via CDN and Babel for rapid prototyping in `base.html`. For production, build and serve compiled assets instead.
- If you accidentally committed the virtualenv or DB, the repository now includes a `.gitignore` that excludes `.venv/` and `db.sqlite3`. To remove tracked copies use `git rm --cached` locally.

## Git / repo notes
- The project is pushed to `https://github.com/AbdulMaaji/django__projects.git` on branch `main`.

## Future work
- Move React code to static JS files and build with a bundler (Vite/webpack).
- Add unit tests for the `todo` app and simple smoke tests for views.

---
If you want, I can also add a `requirements.txt`, wire the React assets into `static/`, or create a small test that verifies the `/news-test/` page serves the style block. Tell me which you'd prefer next.