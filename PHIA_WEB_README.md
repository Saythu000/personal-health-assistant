# 🏥 PHIA Web Application

Complete full-stack Personal Health Insights Agent with React frontend and Flask backend.

## 🚀 Quick Start

### Prerequisites
- Python 3.11+ (already installed)
- Node.js 16+ and npm (install from https://nodejs.org/)

### One-Command Launch
```bash
cd "/mnt/c/Users/User/OneDrive/Desktop/client projects/personal-health-insights-agent-main"
python start_phia_web.py
```

This will:
1. ✅ Start Flask API server (port 5000)
2. ✅ Install React dependencies
3. ✅ Start React frontend (port 3000)
4. ✅ Open browser automatically

## 🌐 Application URLs

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000
- **API Status**: http://localhost:5000/api/status
- **Health Data**: http://localhost:5000/api/health/summary

## 🎯 Features

### Frontend (React + TypeScript)
- ✅ **Health Dashboard** - Real-time metrics display
- ✅ **AI Chat Interface** - Natural language health queries
- ✅ **Responsive Design** - Works on all devices
- ✅ **Real-time Updates** - Live data synchronization
- ✅ **Modern UI** - Clean, professional interface

### Backend (Flask + PHIA Agent)
- ✅ **PHIA AI Agent** - Google Gemini powered insights
- ✅ **Health Data API** - RESTful endpoints
- ✅ **Real-time Chat** - AI-powered health conversations
- ✅ **Synthetic Data** - Pre-loaded test users
- ✅ **CORS Enabled** - Frontend integration ready

## 📱 User Interface

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
│ ┌─────────────────────────────────────────────────────┐ │
│ │ 🤖 PHIA: Hello! I can analyze your health data...  │ │
│ │ 👤 You: How can I improve my sleep quality?        │ │
│ │ 🤖 PHIA: Based on your 7.2h average sleep...       │ │
│ └─────────────────────────────────────────────────────┘ │
│ [Ask me about your health...] [Send]                   │ │
└─────────────────────────────────────────────────────────┘
```

## 🛠️ Manual Setup (Alternative)

### Backend Only
```bash
cd "/mnt/c/Users/User/OneDrive/Desktop/client projects/personal-health-insights-agent-main"
source phia_env/bin/activate
python phia_api_server.py
```

### Frontend Only
```bash
cd phia-frontend
npm install
npm start
```

## 🔧 Development

### Project Structure
```
personal-health-insights-agent-main/
├── phia-frontend/                 # React frontend
│   ├── src/
│   │   ├── components/           # React components
│   │   ├── services/            # API integration
│   │   └── App.tsx              # Main app
│   └── package.json
├── phia_api_server.py            # Flask backend
├── phia_agent.py                 # PHIA AI agent
├── start_phia_web.py             # Full-stack launcher
└── synthetic_wearable_users/     # Test data
```

### API Endpoints
- `GET /api/health/summary` - Health metrics
- `POST /api/chat` - AI chat messages
- `GET /api/status` - Server status

## 🎯 Example Queries

Try asking PHIA:
- "How can I improve my sleep quality?"
- "What's my heart rate trend?"
- "Am I getting enough exercise?"
- "How can I reduce stress?"
- "What's my fitness level?"

## 🔒 Privacy & Security

- All data processed locally
- No external data sharing
- Secure API communication
- Privacy-focused design

## 🚨 Troubleshooting

### Port Already in Use
```bash
# Kill processes on ports 3000 and 5000
lsof -ti:3000 | xargs kill -9
lsof -ti:5000 | xargs kill -9
```

### Missing Dependencies
```bash
# Backend
source phia_env/bin/activate
pip install -r requirements.txt

# Frontend
cd phia-frontend
npm install
```

### Node.js Not Found
Install Node.js from: https://nodejs.org/

---

**🎉 Your PHIA Web Application is ready! Visit http://localhost:3000 to start exploring your health insights!**
