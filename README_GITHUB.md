# 🏥 PHIA - Personal Health Insights Agent

A complete web application that transforms wearable device data into personalized health insights using AI. Built with Flask backend and modern web frontend.

![PHIA Demo](teaser.gif)

## 🌟 Features

- 📊 **Real-time Health Dashboard** - Heart rate, steps, sleep, activity metrics
- 🤖 **AI Health Assistant** - Natural language health consultations
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile
- 🔒 **Privacy-First** - All data processed locally
- ⚡ **Real-time Updates** - Live health data synchronization

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- Virtual environment (included)

### One-Command Launch
```bash
git clone https://github.com/Saythu000/-phia-health-agent.git
cd -phia-health-agent
source phia_env/bin/activate
python phia_simple_app.py
```

**Visit:** http://localhost:5000

## 🎯 Try These Questions

Ask the AI assistant:
- "How can I improve my sleep quality?"
- "What's my heart rate trend?"
- "Am I getting enough exercise?"
- "How can I reduce stress?"

## 🏗️ Architecture

### Frontend
- **HTML5/CSS3/JavaScript** - Modern responsive interface
- **Tailwind CSS** - Utility-first styling
- **Real-time Chat** - WebSocket-like communication

### Backend
- **Flask** - Python web framework
- **PHIA Agent** - AI-powered health insights
- **Pandas** - Health data processing
- **Google Gemini** - AI language model

## 📁 Project Structure

```
phia-health-agent/
├── 🌐 Web Application
│   ├── phia_simple_app.py        # Main Flask server
│   ├── phia_unified_app.py       # Advanced version
│   ├── templates/index.html      # Frontend interface
│   └── static/js/app.js          # JavaScript logic
│
├── 🧠 AI Agent
│   ├── phia_agent.py             # Core AI agent
│   ├── prompt_templates.py       # AI prompts
│   └── data_utils.py             # Data processing
│
├── 📊 Research Data
│   ├── synthetic_wearable_users/ # Test health data
│   ├── few_shots/               # AI training examples
│   └── data/                    # Research datasets
│
└── 📋 Documentation
    ├── README.md                # This file
    ├── QUICK_START.md          # Setup guide
    └── requirements.txt        # Dependencies
```

## 🎨 User Interface

### Health Dashboard
```
┌─────────────────────────────────────────────────────────┐
│ 🏥 PHIA - Personal Health Insights Agent               │
├─────────────────────────────────────────────────────────┤
│ 📊 Health Dashboard                                     │
│ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐        │
│ │💓 72 bpm│ │👟 8,542 │ │😴 7.2h  │ │🔥 45min │        │
│ │Heart Rate│ │ Steps   │ │ Sleep   │ │Active   │        │
│ └─────────┘ └─────────┘ └─────────┘ └─────────┘        │
├─────────────────────────────────────────────────────────┤
│ 💬 AI Health Assistant                                 │
│ [Interactive chat interface with personalized advice]   │
└─────────────────────────────────────────────────────────┘
```

## 🔧 Development

### Run Development Server
```bash
source phia_env/bin/activate
python phia_simple_app.py
```

### API Endpoints
- `GET /api/health/summary` - Health metrics
- `POST /api/chat` - AI chat messages
- `GET /api/status` - Server status

### Environment Setup
```bash
# Create virtual environment
python -m venv phia_env
source phia_env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 🧪 Testing

### Health Data
The application includes synthetic health data for testing:
- User profiles with realistic health metrics
- Activity data (running, walking, cycling)
- Sleep patterns and heart rate data

### AI Responses
Test the AI with various health questions:
- Sleep optimization
- Exercise recommendations
- Stress management
- Cardiovascular health

## 🚀 Deployment

### Local Deployment
```bash
python phia_simple_app.py
```

### Production Deployment
1. Set up production server (AWS, DigitalOcean, etc.)
2. Configure environment variables
3. Use production WSGI server (Gunicorn)
4. Set up reverse proxy (Nginx)

## 📊 Health Insights

The AI provides personalized recommendations for:

- **Sleep Quality** - Bedtime routines, sleep hygiene
- **Cardiovascular Health** - Heart rate optimization
- **Exercise Planning** - Workout recommendations
- **Stress Management** - Relaxation techniques
- **Nutrition Guidance** - Healthy eating habits

## 🔒 Privacy & Security

- ✅ **Local Processing** - All data stays on your device
- ✅ **No External Sharing** - Health data never leaves your server
- ✅ **Secure Communication** - HTTPS ready
- ✅ **Privacy by Design** - Minimal data collection

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

## 🙏 Acknowledgments

- **Google Research** - Original PHIA research
- **Gemini AI** - Language model integration
- **Synthetic Health Data** - Realistic test datasets

## 📞 Support

- Create an issue for bugs or feature requests
- Check documentation for setup help
- Review examples for usage guidance

---

**🎉 Transform your health data into actionable insights with PHIA!**

**Visit: http://localhost:5000 after starting the server**
