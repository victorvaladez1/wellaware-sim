# 🛢️ WellAwareSim

**WellAwareSim** is a backend-only Flask API that simulates oilfield hardware — including oil wells, real-time sensor readings, and fault conditions — to serve as a mock data feed for external applications like dashboards or full-stack OilTech platforms.

This project mimics real-world industrial equipment behavior and supports CRUD operations for wells, real-time anomaly detection, and alert logging.

---

## ⚙️ Tech Stack

- **Python 3.9+**
- **Flask** (REST API)
- **JSON files** as mock storage
- No frontend — this API acts as a simulated external system

---

## 🚀 API Endpoints

### 🛢️ Wells

- `GET /api/wells`  
  Returns a list of all simulated oil wells.

- `POST /api/wells`  
  Adds a new well. Expects:
  ```json
  {
    "name": "Well Delta",
    "location": "South Texas"
  }
  ```

- `DELETE /api/wells/<id>`  
  Removes the well with the specified ID.

---

### 🌡️ Sensor Readings

- `GET /api/readings`  
  Returns real-time randomized sensor data for all wells:
  - `pressure` (psi)
  - `temperature` (°F)
  - `flow_rate` (barrels/hour)
  - `timestamp`
  - `status`: list of any anomalies (e.g. `"HIGH PRESSURE"`, `"LOW FLOW"`)

- `GET /api/readings?well_id=<id>`  
  Returns a single reading for the specified well.

---

### 🚨 Alerts

- `GET /api/alerts`  
  Returns only the readings where anomalies are detected (`status` ≠ `["NORMAL"]`).  
  Also logs those alerts to `alerts.json`.

- `GET /api/alert-log`  
  Returns all saved alerts from `alerts.json`.

- `DELETE /api/alerts`  
  Clears the alert log (resets `alerts.json` to an empty list).

---

## 📁 File Structure

```
wellaware-sim/
├── app/
│   ├── __init__.py         # Flask app factory
│   ├── routes.py           # All API endpoints
│   ├── generator.py        # Sensor data logic
│   ├── wells.json          # Mock well data
│   ├── alerts.json         # Alert log
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
- http://localhost:5000/api/alert-log

---

## 🧠 Purpose

This API simulates real-time oilfield equipment and telemetry for testing, development, and integration with full-stack apps. It can replace hardware during prototyping or serve as a mock microservice in your architecture.

---

## 📛 Author

Built by Victor Valadez  
[GitHub](https://github.com/victorvaladez) • Houston-based SWE
