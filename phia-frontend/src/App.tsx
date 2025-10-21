import React, { useState, useEffect } from 'react';
import HealthMetrics from './components/HealthMetrics';
import ChatInterface from './components/ChatInterface';
import { apiService, HealthSummary } from './services/api';

const App: React.FC = () => {
  const [healthData, setHealthData] = useState<HealthSummary | null>(null);
  const [loading, setLoading] = useState(true);
  const [apiStatus, setApiStatus] = useState<string>('checking');

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      
      // Check API status
      const statusResult = await apiService.getStatus();
      if (statusResult.data) {
        setApiStatus(statusResult.data.status);
      }

      // Fetch health data
      const healthResult = await apiService.getHealthSummary();
      if (healthResult.data) {
        setHealthData(healthResult.data);
      }
      
      setLoading(false);
    };

    fetchData();

    // Refresh data every 30 seconds
    const interval = setInterval(fetchData, 30000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-purple-50">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-800 mb-2">
            🏥 PHIA
          </h1>
          <p className="text-xl text-gray-600">Personal Health Insights Agent</p>
          <div className="flex justify-center items-center mt-2">
            <div className={`w-3 h-3 rounded-full mr-2 ${
              apiStatus === 'running' ? 'bg-green-500' : 'bg-red-500'
            }`}></div>
            <span className="text-sm text-gray-500">
              API Status: {apiStatus === 'running' ? 'Connected' : 'Disconnected'}
            </span>
          </div>
        </div>

        {/* Health Metrics Dashboard */}
        <div className="mb-8">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">📊 Health Dashboard</h2>
          <HealthMetrics healthData={healthData} loading={loading} />
        </div>

        {/* Chat Interface */}
        <div className="max-w-4xl mx-auto">
          <h2 className="text-2xl font-bold text-gray-800 mb-4">💬 AI Health Assistant</h2>
          <ChatInterface />
        </div>

        {/* Footer */}
        <div className="text-center mt-8 text-gray-500 text-sm">
          <p>Powered by Google Gemini AI • Personal Health Insights Agent</p>
          <p className="mt-1">Your health data is processed securely and privately</p>
        </div>
      </div>
    </div>
  );
};

export default App;
