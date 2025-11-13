@echo off
echo.
echo ========================================
echo ETF Investment Simulator - Setup Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://www.python.org
    exit /b 1
)

echo ✓ Python found
python --version

REM Create virtual environment
echo.
echo Creating virtual environment...
if exist venv (
    echo ⚠️  Virtual environment already exists
) else (
    python -m venv venv
    echo ✓ Virtual environment created
)

REM Activate virtual environment
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo.
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install uv
echo.
echo Installing uv (modern package manager)...
pip install uv

REM Install requirements using uv lock file
echo.
echo Installing dependencies from uv.lock (reproducible build)...
uv pip install -r uv.lock

if errorlevel 1 (
    echo ❌ Error: Failed to install dependencies
    exit /b 1
)

echo ✓ Dependencies installed successfully

REM Copy .env file
if exist .env (
    echo ⚠️  .env file already exists
) else (
    if exist .env.example (
        copy .env.example .env
        echo ✓ .env file created from .env.example
    )
)

echo.
echo ========================================
echo ✓ Setup Complete!
echo ========================================
echo.
echo To start the application:
echo   1. Run: venv\Scripts\activate
echo   2. Run: python run.py
echo.
echo The application will be available at:
echo   http://127.0.0.1:5000
echo.
pause
