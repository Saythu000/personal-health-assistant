#!/usr/bin/env python3
"""
PHIA Simple Web Application
Simplified version with intelligent responses without complex agent
"""

from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import pandas as pd
import os
import sys
from datetime import datetime
import random

app = Flask(__name__)
CORS(app)

# Health data
health_summary = {
    'heartRate': 72,
    'steps': 8542,
    'sleep': '7.2h',
    'activeMinutes': 45,
    'calories': 2100
}

def get_intelligent_response(message):
    """Generate intelligent health responses based on message content"""
    message_lower = message.lower()
    
    # Sleep-related responses
    if any(word in message_lower for word in ['sleep', 'tired', 'rest', 'bed', 'wake']):
        responses = [
            f"Based on your {health_summary['sleep']} average sleep, here are some tips to improve sleep quality:\n\n• Maintain a consistent bedtime routine - go to bed and wake up at the same time daily\n• Avoid screens 1 hour before bedtime\n• Keep your bedroom cool (65-68°F) and dark\n• Try relaxation techniques like deep breathing or meditation\n• Avoid caffeine after 2 PM\n\nYour current sleep duration is good, but quality matters too!",
            
            f"Sleep optimization tips for you:\n\n• Create a wind-down routine 30 minutes before bed\n• Consider your {health_summary['activeMinutes']} active minutes - exercise helps sleep, but not too close to bedtime\n• Track your sleep patterns to identify what affects your rest\n• Try magnesium supplements (consult your doctor first)\n• Keep a sleep diary to identify patterns\n\nConsistent sleep timing is key to better rest quality!"
        ]
        return random.choice(responses)
    
    # Heart rate and cardio
    elif any(word in message_lower for word in ['heart', 'cardio', 'cardiovascular', 'pulse']):
        responses = [
            f"Your current resting heart rate is {health_summary['heartRate']} bpm, which is in a healthy range! Here's how to improve cardiovascular health:\n\n• Aim for 150 minutes of moderate exercise weekly\n• Include both cardio and strength training\n• Your {health_summary['steps']} steps today is excellent - keep it up!\n• Try interval training to improve heart efficiency\n• Monitor your heart rate during workouts\n\nA lower resting heart rate often indicates better fitness!",
            
            f"Cardiovascular health insights:\n\n• Your {health_summary['heartRate']} bpm resting heart rate shows good fitness\n• With {health_summary['activeMinutes']} active minutes, you're on track\n• Try activities that elevate your heart rate: brisk walking, cycling, swimming\n• Heart rate variability improves with consistent exercise\n• Stay hydrated and manage stress for optimal heart health\n\nKeep up the great work with your activity levels!"
        ]
        return random.choice(responses)
    
    # Exercise and fitness
    elif any(word in message_lower for word in ['exercise', 'workout', 'fitness', 'active', 'gym', 'run', 'walk']):
        responses = [
            f"Great question about fitness! With {health_summary['activeMinutes']} active minutes and {health_summary['steps']} steps today, you're doing well:\n\n• Mix cardio with strength training 2-3x per week\n• Progressive overload - gradually increase intensity\n• Recovery is crucial - allow rest days\n• Stay consistent rather than intense\n• Listen to your body to avoid overtraining\n\nYour current activity level is impressive - maintain this momentum!",
            
            f"Fitness optimization based on your data:\n\n• Your {health_summary['steps']} daily steps exceed recommendations\n• Add variety: try different activities to prevent boredom\n• Focus on functional movements that help daily life\n• Track progress with metrics beyond just steps\n• Consider your {health_summary['sleep']} sleep - recovery is when muscles grow\n\nBalance is key: activity, nutrition, and rest work together!"
        ]
        return random.choice(responses)
    
    # Stress management
    elif any(word in message_lower for word in ['stress', 'anxiety', 'relax', 'calm', 'mental']):
        responses = [
            f"Stress management is crucial for overall health! Here are evidence-based strategies:\n\n• Regular exercise (you're doing great with {health_summary['activeMinutes']} active minutes!)\n• Deep breathing: 4-7-8 technique (inhale 4, hold 7, exhale 8)\n• Mindfulness meditation - even 5 minutes daily helps\n• Adequate sleep - your {health_summary['sleep']} is good, maintain it\n• Social connections and hobbies\n• Limit caffeine and alcohol\n\nPhysical activity is one of the best stress relievers!",
            
            f"Stress reduction techniques that work:\n\n• Your {health_summary['steps']} steps help release endorphins naturally\n• Progressive muscle relaxation before bed\n• Time in nature - even 10 minutes outdoors helps\n• Journaling to process thoughts\n• Limit news and social media consumption\n• Practice gratitude daily\n\nYour active lifestyle already supports stress management!"
        ]
        return random.choice(responses)
    
    # Weight and nutrition
    elif any(word in message_lower for word in ['weight', 'diet', 'nutrition', 'eat', 'food', 'calories']):
        responses = [
            f"Nutrition and weight management insights:\n\n• Your {health_summary['steps']} steps burn approximately 300-400 calories\n• Focus on whole foods: lean proteins, vegetables, fruits, whole grains\n• Portion control is more important than strict dieting\n• Stay hydrated - often thirst is mistaken for hunger\n• Eat mindfully without distractions\n• Balance calories in vs calories out\n\nCombine your great activity level with consistent nutrition habits!",
            
            f"Healthy eating strategies:\n\n• Plan meals ahead to avoid impulsive choices\n• Include protein with each meal for satiety\n• Your active lifestyle ({health_summary['activeMinutes']} minutes) supports metabolism\n• Don't skip meals - it can lead to overeating later\n• Listen to hunger and fullness cues\n• Allow occasional treats in moderation\n\nConsistency beats perfection in nutrition!"
        ]
        return random.choice(responses)
    
    # General health
    else:
        responses = [
            f"Based on your current health metrics, you're doing well! Here's your snapshot:\n\n• Heart Rate: {health_summary['heartRate']} bpm (healthy range)\n• Steps: {health_summary['steps']} (exceeds daily recommendations)\n• Sleep: {health_summary['sleep']} (good duration)\n• Active Minutes: {health_summary['activeMinutes']} (great job!)\n\nKey areas to focus on:\n• Maintain consistency in your routines\n• Balance activity with adequate recovery\n• Stay hydrated and eat nutrient-dense foods\n• Monitor how you feel, not just the numbers\n\nWhat specific aspect would you like to improve?",
            
            f"Your health profile looks strong! Here's what stands out:\n\n• Excellent daily activity with {health_summary['steps']} steps\n• Good sleep duration at {health_summary['sleep']}\n• Solid cardiovascular health with {health_summary['heartRate']} bpm resting HR\n• {health_summary['activeMinutes']} active minutes shows commitment\n\nTo optimize further:\n• Track trends over time, not just daily numbers\n• Focus on sleep quality, not just quantity\n• Include strength training if not already doing so\n• Consider stress management techniques\n\nYou're on the right track - keep it up!"
        ]
        return random.choice(responses)

# Frontend Routes
@app.route('/')
def index():
    return render_template('index.html')

# API Routes
@app.route('/api/health/summary', methods=['GET'])
def get_health_summary():
    return jsonify(health_summary)

@app.route('/api/chat', methods=['POST'])
def chat_with_phia():
    try:
        data = request.json
        message = data.get('message', '')
        
        if not message:
            return jsonify({'error': 'No message provided'}), 400
        
        response = get_intelligent_response(message)
        
        return jsonify({
            'response': response,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        print(f"Chat error: {e}")
        return jsonify({
            'response': "I'm here to help with your health questions. Please try asking about sleep, exercise, nutrition, or stress management.",
            'error': str(e)
        }), 500

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({
        'status': 'running',
        'phia_agent': 'simplified',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("🏥 Starting PHIA Simple Web Application...")
    print("🚀 PHIA Web Application running at: http://localhost:5000")
    print("💡 Open your browser and visit: http://localhost:5000")
    
    app.run(debug=True, port=5000, host='0.0.0.0')
