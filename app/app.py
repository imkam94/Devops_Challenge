import os
from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# Load credentials from environment variables
USERNAME = os.getenv("API_USERNAME", "admin")
PASSWORD_HASH = generate_password_hash(os.getenv("API_PASSWORD", "password"))

@auth.verify_password
def verify_password(username, password):
    if username == USERNAME and check_password_hash(PASSWORD_HASH, password):
        return username
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

@app.route('/data', methods=['GET'])
@auth.login_required
def data():
    return jsonify({"data": "dummy data"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)