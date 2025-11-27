#!/bin/bash
echo "🚀 Starting AF IMPERIYA Enterprise System..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt > /dev/null 2>&1

# Initialize database
echo "Initializing database..."
python init_db.py

# Start the application
echo ""
echo "✓ Starting application..."
echo "✓ Server running at http://localhost:5000"
echo "✓ Press Ctrl+C to stop"
echo ""
python app.py
