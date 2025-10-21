#!/usr/bin/env python3
"""
PHIA Web Application Launcher
Starts both Flask API server and React frontend
"""

import os
import sys
import subprocess
import threading
import time
import webbrowser

def start_backend():
    """Start Flask API server"""
    print("🔧 Starting PHIA API Server...")
    try:
        # Activate virtual environment and start Flask
        if os.name == 'nt':  # Windows
            activate_cmd = r"phia_env\Scripts\activate"
        else:  # Linux/Mac
            activate_cmd = "source phia_env/bin/activate"
        
        subprocess.run([
            sys.executable, "phia_api_server.py"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Backend failed to start: {e}")

def start_frontend():
    """Start React frontend"""
    print("⚛️  Starting React Frontend...")
    try:
        os.chdir("phia-frontend")
        
        # Install dependencies if needed
        if not os.path.exists("node_modules"):
            print("📦 Installing frontend dependencies...")
            subprocess.run(["npm", "install"], check=True)
        
        # Start React development server
        subprocess.run(["npm", "start"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Frontend failed to start: {e}")
    except FileNotFoundError:
        print("❌ Node.js/npm not found. Please install Node.js first.")

def main():
    print("🏥 PHIA - Personal Health Insights Agent")
    print("=" * 50)
    print("🚀 Starting Full-Stack Web Application...")
    print()
    
    # Check if Node.js is available
    try:
        subprocess.run(["node", "--version"], capture_output=True, check=True)
        subprocess.run(["npm", "--version"], capture_output=True, check=True)
        print("✅ Node.js and npm are available")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Node.js/npm not found!")
        print("Please install Node.js from: https://nodejs.org/")
        return
    
    print("✅ Environment ready")
    print()
    
    # Start backend in a separate thread
    backend_thread = threading.Thread(target=start_backend, daemon=True)
    backend_thread.start()
    
    # Wait a moment for backend to start
    print("⏳ Waiting for backend to initialize...")
    time.sleep(3)
    
    print()
    print("🌐 Application URLs:")
    print("   Frontend: http://localhost:3000")
    print("   Backend API: http://localhost:5000")
    print("   API Status: http://localhost:5000/api/status")
    print()
    
    # Start frontend (this will block)
    try:
        start_frontend()
    except KeyboardInterrupt:
        print("\n👋 Shutting down PHIA Web Application...")

if __name__ == "__main__":
    main()
