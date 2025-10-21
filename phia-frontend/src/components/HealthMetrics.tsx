import React from 'react';
import { HealthSummary } from '../services/api';

interface HealthMetricsProps {
  healthData: HealthSummary | null;
  loading: boolean;
}

const MetricCard: React.FC<{
  icon: string;
  value: string | number;
  label: string;
  color: string;
}> = ({ icon, value, label, color }) => (
  <div className={`bg-white rounded-xl p-6 shadow-lg border-l-4 ${color} transform hover:scale-105 transition-transform duration-200`}>
    <div className="flex items-center justify-between">
      <div>
        <p className="text-2xl font-bold text-gray-800">{value}</p>
        <p className="text-sm text-gray-600 mt-1">{label}</p>
      </div>
      <div className="text-3xl">{icon}</div>
    </div>
  </div>
);

const HealthMetrics: React.FC<HealthMetricsProps> = ({ healthData, loading }) => {
  if (loading) {
    return (
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        {[...Array(4)].map((_, i) => (
          <div key={i} className="bg-white rounded-xl p-6 shadow-lg animate-pulse">
            <div className="h-8 bg-gray-200 rounded mb-2"></div>
            <div className="h-4 bg-gray-200 rounded"></div>
          </div>
        ))}
      </div>
    );
  }

  if (!healthData) {
    return (
      <div className="bg-white rounded-xl p-6 shadow-lg mb-8">
        <p className="text-center text-gray-600">Unable to load health data</p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      <MetricCard
        icon="💓"
        value={`${healthData.heartRate} bpm`}
        label="Heart Rate"
        color="border-red-500"
      />
      <MetricCard
        icon="👟"
        value={healthData.steps.toLocaleString()}
        label="Steps Today"
        color="border-blue-500"
      />
      <MetricCard
        icon="😴"
        value={healthData.sleep}
        label="Sleep Duration"
        color="border-purple-500"
      />
      <MetricCard
        icon="🔥"
        value={`${healthData.activeMinutes}min`}
        label="Active Minutes"
        color="border-orange-500"
      />
    </div>
  );
};

export default HealthMetrics;
