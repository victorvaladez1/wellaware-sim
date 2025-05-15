# 🛢️ WellAwareSim

**WellAwareSim** is a backend-only Flask API that simulates live oilfield hardware — including oil wells, sensor data, and real-time alert generation — to serve as a mock data feed for frontend dashboards or full-stack OilTech applications.

This project is designed to mimic real-world oilfield monitoring systems using dynamically generated sensor readings, anomaly detection, and persistent alert logging.

---

## ⚙️ Tech Stack

- **Python 3.9+**
- **Flask** (REST API)
- **JSON files** as mock storage
- No frontend — backend-only for simulating oil equipment data

---

## 🚀 Features Implemented

### ✅ `GET /api/wells`
Returns a list of oil wells being simulated.

- Wells are stored in `wells.json`
- Each has an ID, name, and location

### ✅ `GET /api/readings`
Returns live simulated sensor readings for all wells.

Each reading includes:
- `pressure` (psi)
- `temperature` (°F)
- `flow_rate` (barrels/hour)
- `timestamp`
- `status`: a list of alert conditions such as:
  - `"HIGH PRESSURE"` (if pressure > 230 psi)
  - `"LOW FLOW"` (if flow_rate < 25)
  - `"HIGH TEMP"` (if temperature > 115°F)
  - or `["NORMAL"]` if no anomalies

### ✅ `GET /api/readings?well_id=1`
Optionally fetch sensor data from a specific well by ID.

### ✅ `GET /api/alerts`
Returns simulated sensor readings for wells with **abnormal conditions** (i.e., status ≠ `["NORMAL"]`).

- Each request triggers new sensor data
- Abnormal readings are also logged to `alerts.json` for history

---

## 📁 File Structure

```
wellaware-sim/
├── app/
│   ├── __init__.py         # Flask app factory
│   ├── routes.py           # All API endpoints
│   ├── generator.py        # Sensor data logic
│   ├── wells.json          # Mock well data
│   ├── alerts.json         # Persistent alert log
├── run.py                  # Entry point for Flask app
├── requirements.txt
├── README.md
```

---

## 📦 Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/your-username/wellaware-sim.git
cd wellaware-sim
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
.env\Scriptsctivate         # Windows
# source venv/bin/activate     # macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
python run.py
```

5. Test endpoints in browser or Postman:
- http://localhost:5000/api/wells
- http://localhost:5000/api/readings
- http://localhost:5000/api/alerts

---

## 🔮 Coming Soon

- `POST /api/wells` to add new test wells dynamically
- `/api/alert-log` to view full alert history
- Time-based readings using background jobs (e.g., every 5 seconds)
- WebSocket stream for live dashboards

---

## 🧠 Purpose

This API is a simulated backend service for OilTech dashboards and monitoring platforms. It was built to:
- Practice realistic REST API design
- Prototype oilfield software without real hardware
- Showcase full-stack readiness for oil & energy tech

---

## 📛 Author

Built with ☕ and 🔧 by Victor Valadez  
[GitHub](https://github.com/victorvaladez) • Houston-based SWE
