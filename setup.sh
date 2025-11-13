#!/bin/bash

echo ""
echo "========================================"
echo "ETF Investment Simulator - Setup Script"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "✓ Python found"
python3 --version

# Create virtual environment
echo ""
echo "Creating virtual environment..."
if [ -d "venv" ]; then
    echo "⚠️  Virtual environment already exists"
else
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo ""
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Install uv
echo ""
echo "Installing uv (modern package manager)..."
pip install uv

# Install requirements using uv lock file
echo ""
echo "Installing dependencies from uv.lock (reproducible build)..."
uv pip install -r uv.lock

if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to install dependencies"
    exit 1
fi

echo "✓ Dependencies installed successfully"

# Copy .env file
if [ -f ".env" ]; then
    echo "⚠️  .env file already exists"
else
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo "✓ .env file created from .env.example"
    fi
fi

echo ""
echo "========================================"
echo "✓ Setup Complete!"
echo "========================================"
echo ""
echo "To start the application:"
echo "  1. Run: source venv/bin/activate"
echo "  2. Run: python run.py"
echo ""
echo "The application will be available at:"
echo "  http://127.0.0.1:5000"
echo ""
