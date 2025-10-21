#!/usr/bin/env python3
"""
PHIA Unified Web Application
Single Flask server serving both frontend and API
"""

from flask import Flask, request, jsonify, render_template, send_from_directory
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
    PHIA_AVAILABLE = True
except ImportError as e:
    print(f"⚠️  Could not import PHIA modules: {e}")
    print("⚠️  Running in fallback mode")
    PHIA_AVAILABLE = False

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
    """Initialize PHIA with synthetic data"""
    global current_agent, health_summary
    
    if not PHIA_AVAILABLE:
        print("⚠️  PHIA not available, using mock data")
        return False
    
    try:
        # Load synthetic user data
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
            print("⚠️  Using sample data - synthetic files not found")
            summary_df = pd.DataFrame({
                'steps': [8542], 'sleep_duration': [7.2], 
                'resting_heart_rate': [72], 'active_minutes': [45]
            })
        
        # Create minimal exercise data
        if os.path.exists(exercise_path):
            activities_df = pd.read_csv(exercise_path)
        else:
            activities_df = pd.DataFrame({
                'activity_type': ['Running'], 'duration': [30], 'calories': [300]
            })
        
        profile_df = pd.DataFrame([{'age': 30, 'gender': 'M'}])
        
        # Initialize PHIA agent
        current_agent = get_react_agent(
            summary_df=summary_df,
            activities_df=activities_df,
            profile_df=profile_df,
            example_files=[],
            use_mock_search=True
        )
        print("✅ PHIA agent initialized")
        return True
        
    except Exception as e:
        print(f"⚠️  Error initializing PHIA: {e}")
        return False

# Frontend Routes
@app.route('/')
def index():
    """Serve the main application"""
    return render_template('index.html')

@app.route('/static/<path:filename>')
def static_files(filename):
    """Serve static files"""
    return send_from_directory('static', filename)

# API Routes
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
        
        if not message:
            return jsonify({'error': 'No message provided'}), 400
        
        if current_agent and PHIA_AVAILABLE:
            try:
                # Execute the agent and get the final result
                agent_result = current_agent(message)
                
                # Extract the final answer from the agent result
                if hasattr(agent_result, 'updates') and agent_result.updates:
                    # Get the last update that contains the final answer
                    for update in reversed(agent_result.updates):
                        if hasattr(update, 'observation') and update.observation and hasattr(update, 'is_finished') and update.is_finished:
                            response = update.observation
                            break
                    else:
                        # If no finished update found, use the last observation
                        last_update = agent_result.updates[-1]
                        if hasattr(last_update, 'observation') and last_update.observation:
                            response = last_update.observation
                        else:
                            response = "I'm processing your health data. Let me provide some general guidance based on your current metrics."
                else:
                    # Fallback if agent structure is different
                    response = "I'm analyzing your health data to provide personalized recommendations."
                    
            except Exception as e:
                print(f"PHIA agent error: {e}")
                response = f"I can help with your health data! You asked: '{message}'. Based on your current metrics - heart rate: {health_summary['heartRate']} bpm, steps: {health_summary['steps']}, sleep: {health_summary['sleep']} - I'd recommend focusing on maintaining consistent sleep patterns and staying active."
        else:
            # Fallback responses based on keywords
            message_lower = message.lower()
            if 'sleep' in message_lower:
                response = f"Based on your {health_summary['sleep']} average sleep duration, I recommend maintaining a consistent bedtime routine. Try to go to bed and wake up at the same time daily, avoid screens 1 hour before bed, and keep your bedroom cool and dark."
            elif 'heart' in message_lower or 'cardio' in message_lower:
                response = f"Your current heart rate is {health_summary['heartRate']} bpm. For cardiovascular health, aim for 150 minutes of moderate exercise weekly. Your {health_summary['steps']} steps today is great - keep it up!"
            elif 'exercise' in message_lower or 'workout' in message_lower:
                response = f"With {health_summary['activeMinutes']} active minutes and {health_summary['steps']} steps today, you're doing well! Try to maintain at least 30 minutes of activity daily. Mix cardio with strength training for best results."
            elif 'stress' in message_lower:
                response = "To reduce stress, try deep breathing exercises, regular physical activity, adequate sleep, and mindfulness practices. Your current activity levels look good - keep maintaining that routine!"
            else:
                response = f"I can help with your health data! You asked: '{message}'. Your current metrics show heart rate: {health_summary['heartRate']} bpm, steps: {health_summary['steps']}, sleep: {health_summary['sleep']}, and {health_summary['activeMinutes']} active minutes. What specific aspect would you like to improve?"
        
        return jsonify({
            'response': response,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        print(f"Chat error: {e}")
        return jsonify({
            'response': f"I encountered an issue processing your request. Please try asking about your health metrics or wellness goals.",
            'error': str(e)
        }), 500

@app.route('/api/status', methods=['GET'])
def get_status():
    """API status"""
    return jsonify({
        'status': 'running',
        'phia_agent': 'available' if (current_agent and PHIA_AVAILABLE) else 'fallback',
        'timestamp': datetime.now().isoformat()
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors by serving the main app"""
    return render_template('index.html')

if __name__ == '__main__':
    print("🏥 Starting PHIA Unified Web Application...")
    print("=" * 50)
    
    # Initialize PHIA
    success = initialize_phia()
    if success:
        print("✅ PHIA agent initialized successfully")
    else:
        print("⚠️  Running in fallback mode with mock responses")
    
    print(f"\n🚀 PHIA Web Application running at: http://localhost:5000")
    print("📊 Health Dashboard: http://localhost:5000")
    print("🤖 AI Chat Interface: Integrated in main page")
    print("📈 API Status: http://localhost:5000/api/status")
    print("\n💡 Open your browser and visit: http://localhost:5000")
    print("=" * 50)
    
    # Run the unified application
    app.run(debug=True, port=5000, host='0.0.0.0')
