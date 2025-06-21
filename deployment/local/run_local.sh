#!/bin/bash
# Local Development Script for Gift Selection Website

echo "🎁 Starting Gift Selection Website locally..."
echo "=============================================="

# Change to project root directory
cd "$(dirname "$0")/../.."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Generate website
echo "🌐 Generating website..."
python3 generate_gift_website.py

# Generate local development pages
echo "🔧 Generating local development pages..."
python3 deployment/local/generate_local_pages.py

# Start backend server
echo "🚀 Starting backend server on http://localhost:5000"
echo "📊 Admin dashboard: http://localhost:8000/admin.html"
echo "🌍 Main website: http://localhost:8000"
echo ""
echo "Press Ctrl+C to stop both servers"
echo ""

# Start backend in background
python3 backend.py &
BACKEND_PID=$!

# Wait a moment for backend to start
sleep 2

# Start frontend server
cd gift_website
python3 -m http.server 8000 &
FRONTEND_PID=$!

# Wait for interrupt
trap "echo ''; echo '🛑 Stopping servers...'; kill $BACKEND_PID $FRONTEND_PID 2>/dev/null; exit" INT

# Keep script running
wait 