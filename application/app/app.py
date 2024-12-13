from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "UP"})

@app.route('/data', methods=['GET'])
def get_data():
    if 'Authorization' not in request.headers:
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify({"data": "dummy data"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
