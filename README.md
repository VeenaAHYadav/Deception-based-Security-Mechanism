# Deception-based-Security-Mechanism
Deception-based cybersecurity system using honeypots (fake login, hidden APIs, and sensitive file traps) to detect and monitor malicious activity with real-time dashboard visualization.

# 🛡️ Deception-Based Security Mechanism

## 📌 Overview
This project implements a **deception-based security system** that detects malicious activity by deploying **honeypots** such as fake login interfaces, hidden endpoints, and sensitive data traps.

Unlike traditional security systems that only block known threats, this system **identifies attackers based on their behavior** when they interact with deceptive components.

---

## 🎯 Objective
The objective of this project is to:
- Detect unauthorized access attempts
- Identify malicious behavior using deception techniques
- Monitor attacker activity in real time
- Generate alerts for high-risk actions

---

## 🧠 Key Concept
The system is based on a simple principle:

> Any interaction with deceptive components is considered suspicious or malicious.

---

## 🏗️ System Architecture

User (Attacker) --> Deceptive Components (Honeypots) --> Logging System --> Detection Engine --> Alert System --> Monitoring Dashboard

---

## 🎭 Deceptive Components (Honeypots)

### 🔐 Fake Login Interface
- Simulates a real corporate login page
- Captures login attempts
- Does not perform actual authentication

---

### 🖥️ Fake Dashboard
- Mimics a real internal company system
- Encourages further interaction
- Contains embedded traps

---

### 🔐 Hidden Admin Endpoint
- `/admin-panel`
- Not visible in UI
- Access indicates malicious intent

---

### 📁 Sensitive File Trap
- `/confidential-data`
- Shown as "Download Password File"
- Designed to lure attackers

---

## ⚙️ Detection Mechanism

The system uses a **rule-based detection engine** (`detector.py`) to analyze behavior.

### Severity Levels:
| Action | Severity |
|--------|--------|
| Login Attempt | MEDIUM |
| Admin Access | HIGH |
| Sensitive File Access | HIGH |
| Repeated Attempts (>3) | CRITICAL |

---

## 📊 Logging & Alerts

### Logs (`logs.json`)
Stores:
- IP Address
- Action
- Severity
- Timestamp

### Alerts (`alerts.json`)
- Stores only HIGH and CRITICAL activities
- Reduces noise and false positives

---

## 🖥️ Real-Time Monitoring Dashboard

Access:http://127.0.0.1:5000/monitor


### Features:
- Live attack monitoring
- Auto-refresh every 3 seconds
- Color-coded severity:
  - 🟢 LOW
  - 🟠 MEDIUM
  - 🔴 HIGH
  - 🔥 CRITICAL

---

## 🚀 How It Works

1. User interacts with system
2. If a honeypot is triggered:
   - Activity is logged
   - Detection engine analyzes behavior
   - Severity is assigned
3. High-risk actions generate alerts
4. Activity is displayed on dashboard

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install flask
```

### 2. Run the application
```bash
python app.py
```
### 3. Open in browser
```bash
http://127.0.0.1:5000
```
### 4. Open monitoring dashboard
```bash
http://127.0.0.1:5000/monitor
```

Author 
VEENA 
