# /app/v1/details
# /app/v1/healthz

from flask import Flask, jsonify
import datetime
import socket

app = Flask("my big application")

@app.route("/app/v1/details")
def details():
    return jsonify({
        "time": datetime.datetime.now().strftime('%Y-%m-%d'),
        "hostname": socket.gethostname()
    })

@app.route("/app/v1/healthz")
def health():
    return jsonify({
        "status": "up",
        "weather": "fine <6",
        "deployed_on": "kubernetes"
    }), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")