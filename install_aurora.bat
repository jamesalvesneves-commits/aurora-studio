@echo off
title Aurora Studio - Instalador
echo Verificando Python...
py --version >nul 2>&1
if errorlevel 1 (
  echo Python nao encontrado. Instale em https://www.python.org/downloads/ e execute novamente.
  pause
  exit /b 1
)
echo Criando ambiente...
py -m venv .venv
call .venv\Scripts\activate.bat
echo Instalando dependencias...
pip install -r requirements.txt
echo Verificando Ollama...
curl -s http://localhost:11434/api/tags >nul 2>&1
if errorlevel 1 (
  echo AVISO: Ollama nao esta respondendo em http://localhost:11434
  echo Instale em https://ollama.com/download e execute: ollama pull llama3.2
)
echo.
echo Aurora Studio pronto. Use run_aurora.bat para abrir.
pause
