@echo off
echo Starting Social Media Platform Development Server...
echo ==================================================

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo Error: Virtual environment not found. Please run setup.bat first.
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Check if migrations are needed
echo Checking for database changes...
python manage.py makemigrations --dry-run --verbosity=0 > nul
if %errorlevel% neq 0 (
    echo Applying new migrations...
    python manage.py makemigrations
    python manage.py migrate
)

echo.
echo Starting development server...
echo Visit http://127.0.0.1:8000 in your browser
echo Press Ctrl+C to stop the server
echo.

python manage.py runserver
