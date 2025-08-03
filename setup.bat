@echo off
echo Setting up Social Media Platform...
echo ===================================

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo Error: Failed to create virtual environment
    pause
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install requirements
echo Installing requirements...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Failed to install requirements
    pause
    exit /b 1
)

REM Run setup script
echo Running setup script...
python setup.py
if %errorlevel% neq 0 (
    echo Error: Setup script failed
    pause
    exit /b 1
)

echo.
echo Setup complete! To start the server, run:
echo   venv\Scripts\activate
echo   python manage.py runserver
echo.
pause
