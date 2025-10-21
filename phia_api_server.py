#!/usr/bin/env python3
"""
PHIA API Server - Flask wrapper for existing PHIA code
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os
import sys
from datetime import datetime

# Add current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from phia_agent import get_react_agent
    print("✅ PHIA modules imported successfully")
except ImportError as e:
    print(f"⚠️  Could not import PHIA modules: {e}")

app = Flask(__name__)
CORS(app)

# Global variables
current_agent = None
health_summary = {
    'heartRate': 72,
    'steps': 8542,
    'sleep': '7.2h',
    'activeMinutes': 45,
    'calories': 2100
}

def initialize_phia():
    """Initialize PHIA with your existing data"""
    global current_agent, health_summary
    
    try:
        # Load your synthetic user data
        summary_path = 'synthetic_wearable_users/summary_df_465.csv'
        exercise_path = 'synthetic_wearable_users/exercise_df_465.csv'
        
        if os.path.exists(summary_path):
            summary_df = pd.read_csv(summary_path)
            print(f"✅ Loaded summary data: {len(summary_df)} records")
            
            # Update health summary from real data
            latest = summary_df.iloc[-1]
            health_summary.update({
                'heartRate': int(latest.get('resting_heart_rate', 72)),
                'steps': int(latest.get('steps', 8542)),
                'sleep': f"{latest.get('sleep_duration', 7.2):.1f}h",
                'activeMinutes': int(latest.get('active_minutes', 45))
            })
        else:
            print("⚠️  Using sample data - files not found")
            summary_df = pd.DataFrame({
                'steps': [8542], 'sleep_duration': [7.2], 
                'resting_heart_rate': [72], 'active_minutes': [45]
            })
        
        # Create minimal exercise data
        activities_df = pd.DataFrame({
            'activity_type': ['Running'], 'duration': [30], 'calories': [300]
        })
        
        profile_df = pd.DataFrame([{'age': 30, 'gender': 'M'}])
        
        # Initialize PHIA agent
        current_agent = get_react_agent(
            summary_df=summary_df,
            activities_df=activities_df,
            profile_df=profile_df,
            example_files=[],  # Start with no examples
            use_mock_search=True
        )
        print("✅ PHIA agent initialized")
        return True
        
    except Exception as e:
        print(f"⚠️  Error initializing PHIA: {e}")
        return False

@app.route('/api/health/summary', methods=['GET'])
def get_health_summary():
    """Get health summary for dashboard"""
    return jsonify(health_summary)

@app.route('/api/chat', methods=['POST'])
def chat_with_phia():
    """Handle chat with PHIA agent"""
    try:
        data = request.json
        message = data.get('message', '')
        
        if current_agent:
            response = str(current_agent(message))
        else:
            response = f"I can help with your health data! You asked: '{message}'. Your current metrics show heart rate: {health_summary['heartRate']} bpm, steps: {health_summary['steps']}, sleep: {health_summary['sleep']}."
        
        return jsonify({
            'response': response,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'response': f"I encountered an issue: {str(e)}. Please try asking about your health metrics.",
            'error': str(e)
        }), 500

@app.route('/api/status', methods=['GET'])
def get_status():
    """API status"""
    return jsonify({
        'status': 'running',
        'phia_agent': 'available' if current_agent else 'fallback',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'PHIA API Server is running!',
        'endpoints': {
            'health': '/api/health/summary',
            'chat': '/api/chat',
            'status': '/api/status'
        }
    })

if __name__ == '__main__':
    print("🏥 Starting PHIA API Server...")
    
    # Initialize PHIA
    success = initialize_phia()
    print(f"{'✅' if success else '⚠️'} PHIA {'initialized' if success else 'fallback mode'}")
    
    print("\n🚀 Server running at: http://localhost:5000")
    print("📊 Test health data: http://localhost:5000/api/health/summary")
    print("💬 Test chat: POST to http://localhost:5000/api/chat")
    print("📈 Status: http://localhost:5000/api/status")
    
    app.run(debug=True, port=5000, host='0.0.0.0')
