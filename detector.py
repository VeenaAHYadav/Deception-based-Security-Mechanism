from datetime import datetime

def analyze_activity(ip, action, data):
    severity = "LOW"

    if action == "LOGIN_ATTEMPT":
        severity = "MEDIUM"

    if action == "ADMIN_API":
        severity = "HIGH"

    if action == "FILE_ACCESS":
        severity = "HIGH"

    if data.get("attempts", 0) > 3:
        severity = "CRITICAL"

    return {
        "ip": ip,
        "action": action,
        "severity": severity,
        "timestamp": str(datetime.now())
    }