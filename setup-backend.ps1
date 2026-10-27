$ErrorActionPreference = 'Stop'

Set-Location $PSScriptRoot

if (-not (Test-Path '.venv\Scripts\python.exe')) {
    Write-Host '[1/4] Creating virtual environment...' -ForegroundColor Cyan
    py -m venv .venv
}

$python = Join-Path $PSScriptRoot '.venv\Scripts\python.exe'
Write-Host '[2/4] Installing dependencies...' -ForegroundColor Cyan
& $python -m pip install -r requirements.txt

if (-not (Test-Path '.env')) {
    Copy-Item '.env.example' '.env'
    Write-Host 'Created .env from .env.example. Add AI_API_KEY when ready.' -ForegroundColor Yellow
}

Write-Host '[3/4] Applying migrations...' -ForegroundColor Cyan
& $python backend\manage.py migrate --noinput

Write-Host '[4/4] Checking backend...' -ForegroundColor Cyan
& $python backend\manage.py check

Write-Host 'Backend setup complete. Start it with:' -ForegroundColor Green
Write-Host '.\.venv\Scripts\python.exe backend\manage.py runserver 127.0.0.1:8000'
