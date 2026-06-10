from flask import Flask, jsonify
import os
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({
        "service": "infra-lab",
        "status": "running",
        "host": os.getenv("HOSTNAME", "unknown")
    })


@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/time")
def current_time():
    now = datetime.datetime.now().isoformat()
    return jsonify({"current_time": now})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
