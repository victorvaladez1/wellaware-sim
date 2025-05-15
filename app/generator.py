import random
import datetime

def generate_sensor_reading(well_id):
    return {
        "well_id": well_id,
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "pressure": round(random.uniform(100, 250), 2),     #psi
        "temperature": round(random.uniform(70, 120), 2),   # F
        "flow_rate": round(random.uniform(20, 50), 2),      # barrels/hours
    }

def get_all_wells():
    return [
        {"id": 1, "name": "Well Alpha", "location": "West Texas"},
        {"id": 2, "name": "Well Bravo", "location": "East Texas"},
        {"id": 3, "name": "Well Charlie", "location": "New Mexico"},
    ]