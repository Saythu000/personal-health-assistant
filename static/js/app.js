// PHIA Frontend JavaScript Application
class PHIAApp {
    constructor() {
        this.isLoading = false;
        this.messageCount = 1;
        this.init();
    }

    async init() {
        // Set initial timestamp
        document.getElementById('initial-time').textContent = new Date().toLocaleTimeString();
        
        // Load health data
        await this.loadHealthData();
        
        // Check API status
        await this.checkApiStatus();
        
        // Set up auto-refresh
        setInterval(() => this.loadHealthData(), 30000); // Refresh every 30 seconds
    }

    async loadHealthData() {
        try {
            const response = await fetch('/api/health/summary');
            const data = await response.json();
            
            if (response.ok) {
                this.renderHealthMetrics(data);
            } else {
                console.error('Failed to load health data:', data);
            }
        } catch (error) {
            console.error('Error loading health data:', error);
            this.renderHealthMetricsError();
        }
    }

    renderHealthMetrics(data) {
        const container = document.getElementById('health-metrics');
        container.innerHTML = `
            <div class="bg-white rounded-xl p-6 shadow-lg border-l-4 border-red-500 metric-card">
                <div class="flex items-center justify-between">
                    <div>
                        <p class="text-2xl font-bold text-gray-800">${data.heartRate} bpm</p>
                        <p class="text-sm text-gray-600 mt-1">Heart Rate</p>
                    </div>
                    <div class="text-3xl">💓</div>
                </div>
            </div>
            <div class="bg-white rounded-xl p-6 shadow-lg border-l-4 border-blue-500 metric-card">
                <div class="flex items-center justify-between">
                    <div>
                        <p class="text-2xl font-bold text-gray-800">${data.steps.toLocaleString()}</p>
                        <p class="text-sm text-gray-600 mt-1">Steps Today</p>
                    </div>
                    <div class="text-3xl">👟</div>
                </div>
            </div>
            <div class="bg-white rounded-xl p-6 shadow-lg border-l-4 border-purple-500 metric-card">
                <div class="flex items-center justify-between">
                    <div>
                        <p class="text-2xl font-bold text-gray-800">${data.sleep}</p>
                        <p class="text-sm text-gray-600 mt-1">Sleep Duration</p>
                    </div>
                    <div class="text-3xl">😴</div>
                </div>
            </div>
            <div class="bg-white rounded-xl p-6 shadow-lg border-l-4 border-orange-500 metric-card">
                <div class="flex items-center justify-between">
                    <div>
                        <p class="text-2xl font-bold text-gray-800">${data.activeMinutes}min</p>
                        <p class="text-sm text-gray-600 mt-1">Active Minutes</p>
                    </div>
                    <div class="text-3xl">🔥</div>
                </div>
            </div>
        `;
    }

    renderHealthMetricsError() {
        const container = document.getElementById('health-metrics');
        container.innerHTML = `
            <div class="col-span-full bg-white rounded-xl p-6 shadow-lg">
                <p class="text-center text-gray-600">Unable to load health data</p>
            </div>
        `;
    }

    async checkApiStatus() {
        try {
            const response = await fetch('/api/status');
            const data = await response.json();
            
            const indicator = document.getElementById('status-indicator');
            const statusText = document.getElementById('status-text');
            
            if (response.ok && data.status === 'running') {
                indicator.className = 'w-3 h-3 rounded-full mr-2 bg-green-500';
                statusText.textContent = 'Connected';
            } else {
                indicator.className = 'w-3 h-3 rounded-full mr-2 bg-red-500';
                statusText.textContent = 'Disconnected';
            }
        } catch (error) {
            console.error('Error checking API status:', error);
            document.getElementById('status-indicator').className = 'w-3 h-3 rounded-full mr-2 bg-red-500';
            document.getElementById('status-text').textContent = 'Disconnected';
        }
    }

    async sendMessage() {
        const input = document.getElementById('message-input');
        const message = input.value.trim();
        
        if (!message || this.isLoading) return;

        // Hide suggested questions after first message
        if (this.messageCount === 1) {
            document.getElementById('suggested-questions').style.display = 'none';
        }

        // Add user message to chat
        this.addMessageToChat(message, true);
        
        // Clear input and show loading
        input.value = '';
        this.setLoading(true);

        try {
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message })
            });

            const data = await response.json();
            
            if (response.ok) {
                this.addMessageToChat(data.response, false, data.timestamp);
            } else {
                this.addMessageToChat('Sorry, I encountered an issue. Please try again.', false);
            }
        } catch (error) {
            console.error('Chat error:', error);
            this.addMessageToChat('Sorry, I encountered an issue. Please try again.', false);
        } finally {
            this.setLoading(false);
        }

        this.messageCount++;
    }

    addMessageToChat(message, isUser, timestamp = null) {
        const chatContainer = document.getElementById('chat-messages');
        const messageDiv = document.createElement('div');
        
        const timeStr = timestamp ? new Date(timestamp).toLocaleTimeString() : new Date().toLocaleTimeString();
        
        messageDiv.className = `flex ${isUser ? 'justify-end' : 'justify-start'}`;
        messageDiv.innerHTML = `
            <div class="max-w-xs lg:max-w-md px-4 py-2 rounded-lg ${
                isUser ? 'bg-blue-500 text-white' : 'bg-gray-100 text-gray-800'
            }">
                <p class="text-sm">${message}</p>
                <p class="text-xs opacity-70 mt-1">${timeStr}</p>
            </div>
        `;
        
        chatContainer.appendChild(messageDiv);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }

    setLoading(loading) {
        this.isLoading = loading;
        const indicator = document.getElementById('thinking-indicator');
        const sendButton = document.getElementById('send-button');
        const input = document.getElementById('message-input');
        
        if (loading) {
            indicator.classList.remove('hidden');
            sendButton.disabled = true;
            input.disabled = true;
        } else {
            indicator.classList.add('hidden');
            sendButton.disabled = false;
            input.disabled = false;
        }
    }

    handleKeyPress(event) {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault();
            this.sendMessage();
        }
    }

    setMessage(message) {
        document.getElementById('message-input').value = message;
    }
}

// Global functions for HTML event handlers
let app;

function sendMessage() {
    app.sendMessage();
}

function handleKeyPress(event) {
    app.handleKeyPress(event);
}

function setMessage(message) {
    app.setMessage(message);
}

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    app = new PHIAApp();
});
