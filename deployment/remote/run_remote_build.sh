#!/bin/bash
set -e

echo "🎁 Gift Selection System - Remote Build & Deploy"
echo "================================================"

# Change to project root directory
cd "$(dirname "$0")/../.."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Check if required files exist
if [ ! -f "gifts-catalog.csv" ]; then
    echo "❌ gifts-catalog.csv not found!"
    exit 1
fi

if [ ! -f "generate_gift_website.py" ]; then
    echo "❌ generate_gift_website.py not found!"
    exit 1
fi

# Generate production HTML files
echo "🔄 Generating production HTML files..."
python3 generate_gift_website.py

# Verify no localhost references in generated files
echo "🔍 Verifying no localhost references in generated files..."
if grep -r -E "localhost:|127\.0\.0\.1" gift_website/*.html; then
    echo "❌ ERROR: Localhost references found in HTML files! Aborting deployment."
    echo "   This indicates the files were generated for local development, not production."
    exit 1
fi

echo "✅ Production files generated successfully with relative URLs"

# Check if deploy script exists
if [ ! -f "deployment/remote/deploy.sh" ]; then
    echo "❌ deploy.sh not found!"
    exit 1
fi

# Deploy to AWS
echo "🚀 Deploying to AWS..."
cd deployment/remote
./deploy.sh

echo "✅ Remote build and deployment completed successfully!"
echo "🌐 Your gift selection system is now live on AWS!" 