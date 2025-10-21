# 🏥 PHIA - Quick Start Guide

## 🚀 One-Command Launch

```bash
cd "/mnt/c/Users/User/OneDrive/Desktop/client projects/personal-health-insights-agent-main"
python3 run_phia.py
```

**That's it!** Your PHIA web application will start at: **http://localhost:5000**

## 🌟 What You'll See

### Health Dashboard
- 💓 **Heart Rate**: Real-time monitoring
- 👟 **Steps**: Daily step count
- 😴 **Sleep**: Sleep duration tracking  
- 🔥 **Active Minutes**: Exercise tracking

### AI Chat Interface
- 🤖 **Smart Health Assistant**
- 💬 **Natural Language Queries**
- 📊 **Personalized Recommendations**
- ⚡ **Real-time Responses**

## 💡 Try These Questions

- "How can I improve my sleep quality?"
- "What's my heart rate trend?"
- "Am I getting enough exercise?"
- "How can I reduce stress?"

## 🔧 Alternative Launch Methods

### Direct Python
```bash
python3 phia_unified_app.py
```

### With Virtual Environment
```bash
source phia_env/bin/activate
python phia_unified_app.py
```

## 📱 Features

✅ **Single Server** - Everything runs on port 5000  
✅ **No Setup Required** - Works out of the box  
✅ **Real-time Data** - Live health metrics  
✅ **AI-Powered Chat** - Intelligent health insights  
✅ **Mobile Responsive** - Works on all devices  
✅ **Secure & Private** - All data processed locally  

## 🚨 Troubleshooting

### Port Already in Use
```bash
lsof -ti:5000 | xargs kill -9
```

### Python Not Found
Try `python` instead of `python3`:
```bash
python run_phia.py
```

### Missing Dependencies
```bash
pip install flask flask-cors pandas
```

---

**🎉 Your PHIA Health Insights Agent is ready!**  
**Visit: http://localhost:5000**
