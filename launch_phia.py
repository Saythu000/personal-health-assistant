#!/usr/bin/env python3
"""
PHIA Launcher - Simple script to start the Personal Health Insights Agent
"""

import os
import sys
import subprocess

def main():
    print("🏥 PHIA - Personal Health Insights Agent")
    print("=" * 45)
    
    # Set environment variables
    os.environ['GEMINI_API_KEY'] = "AIzaSyA6kG2ljawZ40iu2zs2-_iy92KV9SGSFRk"
    os.environ['GOOGLE_API_KEY'] = "AIzaSyA6kG2ljawZ40iu2zs2-_iy92KV9SGSFRk"
    
    print("✅ API keys configured")
    print("✅ Environment ready")
    print()
    
    # Test imports quickly
    try:
        import pandas as pd
        import google.generativeai as genai
        import ipywidgets
        print("✅ All dependencies available")
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Run: python setup_environment.py")
        return
    
    print()
    print("🚀 Starting Jupyter Notebook...")
    print("📝 Opening phia_demo_configured.ipynb")
    print()
    print("💡 Make sure to select 'PHIA Environment' kernel!")
    print()
    
    # Start Jupyter with the specific notebook
    try:
        subprocess.run([
            "jupyter", "notebook", 
            "phia_demo_configured.ipynb",
            "--NotebookApp.kernel_name=phia_env"
        ], check=True)
    except subprocess.CalledProcessError:
        print("❌ Failed to start Jupyter")
        print("Try manually: jupyter notebook phia_demo_configured.ipynb")

if __name__ == "__main__":
    main()
