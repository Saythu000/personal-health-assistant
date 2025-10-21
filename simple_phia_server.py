#!/usr/bin/env python3
"""
Simple PHIA API Server for Testing
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Sample health data
health_data = {
    'heartRate': 72,
    'steps': 8542,
    'sleep': '7.2h',
    'activeMinutes': 45,
    'calories': 2100
}

@app.route('/')
def home():
    return jsonify({
        'message': 'PHIA API Server is running!',
        'status': 'success',
        'endpoints': ['/api/health/summary', '/api/chat', '/api/status']
    })

@app.route('/api/health/summary')
def get_health_summary():
    return jsonify(health_data)

@app.route('/api/status')
def get_status():
    return jsonify({
        'status': 'running',
        'phia_agent': 'available',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        message = data.get('message', '')
        
        # Simple response based on message
        if 'heart' in message.lower():
            response = f"Your heart rate is {health_data['heartRate']} bpm, which is in a healthy range."
        elif 'sleep' in message.lower():
            response = f"You slept {health_data['sleep']} last night. That's good!"
        elif 'steps' in message.lower():
            response = f"You've taken {health_data['steps']} steps today. Great job!"
        else:
            response = f"I can help with your health data! You asked: '{message}'. Your metrics: Heart Rate: {health_data['heartRate']} bpm, Steps: {health_data['steps']}, Sleep: {health_data['sleep']}"
        
        return jsonify({
            'response': response,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("🏥 PHIA Simple API Server Starting...")
    print("🚀 Server will run at: http://localhost:5000")
    print("📊 Test: http://localhost:5000/api/health/summary")
    
    app.run(debug=True, port=5000, host='127.0.0.1')
