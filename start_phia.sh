#!/bin/bash
# PHIA Startup Script with API Key Configuration

echo "🚀 Starting PHIA (Personal Health Insights Agent)..."

# Navigate to project directory
cd "/mnt/c/Users/User/OneDrive/Desktop/client projects/personal-health-insights-agent-main"

# Activate virtual environment
source phia_env/bin/activate

# Set environment variables
export GEMINI_API_KEY="AIzaSyA6kG2ljawZ40iu2zs2-_iy92KV9SGSFRk"
export GOOGLE_API_KEY="AIzaSyA6kG2ljawZ40iu2zs2-_iy92KV9SGSFRk"

echo "✅ Environment activated and API key configured!"
echo ""
echo "📋 Available options:"
echo "  1. jupyter notebook phia_demo_configured.ipynb  # Pre-configured demo"
echo "  2. jupyter notebook phia_demo.ipynb             # Original demo"
echo "  3. python -c \"import phia_agent; print('Ready!')\" # Test installation"
echo ""
echo "🔑 API Key Status: ✅ Configured"
echo "📊 Synthetic Users Available: 465, 333, 171, 41"
echo ""
echo "🎯 Quick Start:"
echo "  jupyter notebook phia_demo_configured.ipynb"
echo ""

# Keep shell open
exec bash
