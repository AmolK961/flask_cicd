from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        "message": "Hello from Docker CI/CD Pipeline! 🚀",
        "status": "success",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "2.0"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "uptime": "100%"})

@app.route('/api/users')
def users():
    return jsonify([
        {"id": 1, "name": "Amol Kharat", "role": "DevOps Engineer"},
        {"id": 2, "name": "Test User", "role": "YouTuber"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)