@echo off
title Aurora Studio
if not exist .venv (
  echo Execute install_aurora.bat primeiro.
  pause
  exit /b 1
)
call .venv\Scripts\activate.bat
python -m aurora.main
pause
