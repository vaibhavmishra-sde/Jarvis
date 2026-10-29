# Jarvis Command Center

Jarvis is a Django-based AI engineering workspace for conversations, memory, agent orchestration, and operational visibility.

## AI provider



The backend uses an OpenAI-compatible `/chat/completions` gateway with no vendor-specific SDK dependency.

Configure the provider before starting the server:

```powershell
$env:AI_API_KEY = "your-api-key"
$env:AI_BASE_URL = "https://api.openai.com/v1"
$env:AI_MODEL = "gpt-4o-mini"
```

You can also use the **API SETUP** control in the command deck for the same three-step
flow. The browser only displays whether the gateway is configured; it never receives or
stores the secret. Never paste a live key into HTML, JavaScript, Git, or a chat prompt.

For a complete local configuration reference, copy `.env.example` to your environment and replace the development secret key. In production, set `DJANGO_DEBUG=false` and provide an explicit `DJANGO_ALLOWED_HOSTS` list.

Any compatible gateway can be used by changing `AI_BASE_URL` and `AI_MODEL`.

## Run

For a fresh Windows checkout, run the setup script once:

```powershell
.\setup-backend.ps1
```

The script creates `.venv`, installs dependencies, creates `.env` from the
example configuration, applies migrations, and runs Django's system checks.
The backend reads `.env` automatically; process-level environment variables
still take precedence.

Start the development server with:

```powershell
.\.venv\Scripts\python.exe backend\manage.py runserver 127.0.0.1:8000
```

The health probe is available at `GET /api/health/` and reports database, provider, model, and configuration status.
The compact command-center metrics endpoint is available at `GET /api/metrics/`.

## Structure

- `frontend/templates` — command-center interface
- `frontend/static` — CSS and chat client
- `backend/todo` — conversations, AI gateway, and health API
- `backend/db.sqlite3` — development database
## Current skills

Jarvis supports time/date, greetings, jokes, web/Wikipedia/YouTube links, website shortcuts,
to-dos, notes, reminders, persistent memories, weather, and a news briefing. Use `help` in the
command console to see the local skills.

The JSON endpoints are `/api/health/`, `/api/productivity/`, and `/api/briefing/?location=New%20Delhi`.

Tasks can be marked complete with a JSON `PATCH` request to
`/api/productivity/todos/<id>/` using `{"completed": true}`. The endpoint validates the
payload and updates only the completion field.

Chat prompts are limited to 4,000 characters to keep provider requests predictable. The health endpoint includes database connectivity and AI configuration status for lightweight monitoring.

Run the test suite with `python backend/manage.py test todo`.

## Adding a skill

For a small local command, add a focused matcher/handler in `backend/todo/views.py` and cover it
with a test in `backend/todo/tests.py`. For persistent data, add a model and migration, then expose
only the smallest required API endpoint. Keep secrets in environment variables; never commit keys.

## Website shortcuts

Jarvis can open commonly used websites directly from the command console. Try
`open google`, `open youtube`, `open gmail`, `open github`, or `open wikipedia`.
For other sites, use a full domain such as `open example.com`.

## Voice and audio

Use Chrome or Edge on `127.0.0.1` and allow microphone access. `START VOICE` enables speech
recognition, `SPEAK REPLIES` enables speech synthesis, and the audio control remembers mute state.
The allowed startup theme is `frontend/static/audio/jarvis-theme.mp3` and plays once after user
interaction because browsers block autoplay. Double-click the audio status control to open
the volume panel; the level is stored locally in the browser, and ambient looping is opt-in.
