from flask import Flask, jsonify, request
import json
from functools import wraps

app = Flask(__name__)

# Dummy credentials for basic authentication
USERNAME = "admin"
PASSWORD = "secret"

# Load dummy data
with open("dummy_data.json", "r") as f:
    DUMMY_DATA = json.load(f)

# Basic authentication decorator
def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or auth.username != USERNAME or auth.password != PASSWORD:
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return decorated

# Health check endpoint
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "message": "Application is running"}), 200

# Data retrieval endpoint with authentication
@app.route('/data', methods=['GET'])
@require_auth
def get_data():
    return jsonify(DUMMY_DATA), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    