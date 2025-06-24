from flask import Flask, request
import time
import json
import os

app = Flask(__name__)
LOG_FILE = "attack_received_logs.json"

def log_attack(data):
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append({
        "payload": data,
        "timestamp": time.time(),
        "ip": request.remote_addr,
        "user_agent": request.headers.get('User-Agent')
    })

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)

@app.route("/", methods=["GET"])
def index():
    return """
    <html>
        <body>
            <h1>Welcome to the Vulnerable Comment Server♡</h1>
            <form action="/comment" method="POST">
                <input name="comment" placeholder="書いてね…" />
                <input type="submit" value="送信！" />
            </form>
        </body>
    </html>"""


@app.route("/comment", methods=["POST"])
def comment():
    payload = request.form.get("comment", "")
    log_attack(payload)
    return f"<html><body>受け取ったよ：{payload}</body></html>"

if __name__ == "__main__":
    app.run(port=5000)