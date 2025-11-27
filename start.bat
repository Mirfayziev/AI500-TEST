@echo off
echo Starting AF IMPERIYA Enterprise System...
echo.

if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo Initializing database...
python init_db.py

echo.
echo Server running at http://localhost:5000
echo Press Ctrl+C to stop
echo.
python app.py
