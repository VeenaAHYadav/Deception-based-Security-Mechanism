from flask import Flask, request, render_template, jsonify
import json
from detector import analyze_activity

app = Flask(__name__)

LOG_FILE = "logs.json"
ALERT_FILE = "alerts.json"

ip_attempts = {}

# Load logs
def load_logs():
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_log(entry):
    logs = load_logs()
    logs.append(entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

def save_alert(alert):
    try:
        with open(ALERT_FILE, "r") as f:
            alerts = json.load(f)
    except:
        alerts = []

    alerts.append(alert)

    with open(ALERT_FILE, "w") as f:
        json.dump(alerts, f, indent=4)

@app.route("/", methods=["GET", "POST"])
def fake_login():
    ip = request.remote_addr

    if request.method == "POST":
        username = request.form.get("username")

        ip_attempts[ip] = ip_attempts.get(ip, 0) + 1

        activity = analyze_activity(
            ip,
            "LOGIN_ATTEMPT",
            {"attempts": ip_attempts[ip]}
        )

        save_log(activity)

        if activity["severity"] in ["HIGH", "CRITICAL"]:
            save_alert(activity)

        return render_template("dashboard.html")

    return render_template("login.html")


# 🔐 Admin trap
@app.route("/admin-panel")
def admin_trap():
    ip = request.remote_addr

    activity = analyze_activity(ip, "ADMIN_API", {})
    save_log(activity)
    save_alert(activity)

    return jsonify({"error": "Unauthorized access"})


# 📁 File trap
@app.route("/confidential-data")
def fake_file():
    ip = request.remote_addr

    activity = analyze_activity(ip, "FILE_ACCESS", {})
    save_log(activity)
    save_alert(activity)

    return "🚫 Access Denied"


# 📊 View logs (optional)
@app.route("/dashboard-data")
def dashboard_data():
    return jsonify(load_logs())

@app.route("/monitor")
def monitor():
    return render_template("monitor.html")


if __name__ == "__main__":
    app.run(debug=True)
    
    
