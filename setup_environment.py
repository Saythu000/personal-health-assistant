#!/usr/bin/env python3
"""
Setup script for PHIA (Personal Health Insights Agent)
Ensures all dependencies are properly installed and configured.
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return None

def main():
    print("🚀 Setting up PHIA Environment...")
    print("=" * 50)
    
    # Check if we're in a virtual environment
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Virtual environment detected")
    else:
        print("⚠️  Not in virtual environment. Activating phia_env...")
        
    # Install/upgrade required packages
    packages = [
        "pandas==2.3.3",
        "numpy",
        "matplotlib", 
        "scipy",
        "seaborn",
        "google-generativeai",
        "immutabledict",
        "pillow",
        "dataclasses-json",
        "termcolor",
        "aenum",
        "absl-py",
        "jinja2",
        "pyyaml",
        "nbformat",
        "tavily-python",
        "ipywidgets",
        "ipykernel"
    ]
    
    for package in packages:
        run_command(f"pip install {package}", f"Installing {package}")
    
    # Register kernel
    run_command(
        "python -m ipykernel install --user --name=phia_env --display-name='PHIA Environment'",
        "Registering Jupyter kernel"
    )
    
    # Test imports
    print("\n🧪 Testing imports...")
    try:
        import pandas as pd
        import google.generativeai as genai
        import ipywidgets
        from IPython.display import HTML, display
        print("✅ All critical imports successful!")
        print(f"   - Pandas: {pd.__version__}")
        print(f"   - Google GenerativeAI: {genai.__version__}")
        print(f"   - IPywidgets: {ipywidgets.__version__}")
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Start Jupyter: jupyter notebook")
    print("2. Open: phia_demo_configured.ipynb")
    print("3. Select kernel: 'PHIA Environment' from Kernel menu")
    
    return True

if __name__ == "__main__":
    main()
