const API_BASE_URL = process.env.NODE_ENV === 'production' 
  ? 'http://localhost:5000' 
  : 'http://localhost:5000';

export interface HealthSummary {
  heartRate: number;
  steps: number;
  sleep: string;
  activeMinutes: number;
  calories: number;
}

export interface ChatMessage {
  id: string;
  message: string;
  response: string;
  timestamp: string;
  isUser: boolean;
}

export interface ApiResponse<T> {
  data?: T;
  error?: string;
}

class ApiService {
  private async fetchApi<T>(endpoint: string, options?: RequestInit): Promise<ApiResponse<T>> {
    try {
      const response = await fetch(`${API_BASE_URL}${endpoint}`, {
        headers: {
          'Content-Type': 'application/json',
          ...options?.headers,
        },
        ...options,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      return { data };
    } catch (error) {
      console.error(`API Error (${endpoint}):`, error);
      return { error: error instanceof Error ? error.message : 'Unknown error' };
    }
  }

  async getHealthSummary(): Promise<ApiResponse<HealthSummary>> {
    return this.fetchApi<HealthSummary>('/api/health/summary');
  }

  async sendChatMessage(message: string): Promise<ApiResponse<{ response: string; timestamp: string }>> {
    return this.fetchApi('/api/chat', {
      method: 'POST',
      body: JSON.stringify({ message }),
    });
  }

  async getStatus(): Promise<ApiResponse<{ status: string; phia_agent: string; timestamp: string }>> {
    return this.fetchApi('/api/status');
  }
}

export const apiService = new ApiService();
