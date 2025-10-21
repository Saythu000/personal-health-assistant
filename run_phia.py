#!/usr/bin/env python3
"""
Simple PHIA Launcher - Start the unified web application
"""

import os
import sys
import subprocess

def main():
    print("🏥 PHIA - Personal Health Insights Agent")
    print("=" * 45)
    print("🚀 Starting Unified Web Application...")
    print()
    
    # Set environment variables if .env exists
    env_file = '.env'
    if os.path.exists(env_file):
        print("✅ Loading environment variables")
        with open(env_file, 'r') as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value
    
    print("✅ Environment ready")
    print()
    print("🌐 Application will be available at:")
    print("   http://localhost:5000")
    print()
    print("💡 Features available:")
    print("   📊 Health Dashboard")
    print("   🤖 AI Chat Interface") 
    print("   📈 Real-time Health Metrics")
    print()
    
    try:
        # Run the unified application
        subprocess.run([sys.executable, "phia_unified_app.py"], check=True)
    except KeyboardInterrupt:
        print("\n👋 Shutting down PHIA Web Application...")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error starting application: {e}")
        print("Try running directly: python phia_unified_app.py")

if __name__ == "__main__":
    main()
