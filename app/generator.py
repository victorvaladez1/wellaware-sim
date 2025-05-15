import random
import datetime
import json
import os

def generate_sensor_reading(well_id):
    return {
        "well_id": well_id,
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "pressure": round(random.uniform(100, 250), 2),     #psi
        "temperature": round(random.uniform(70, 120), 2),   # F
        "flow_rate": round(random.uniform(20, 50), 2),      # barrels/hours
    }

def get_all_wells():
    json_path = os.path.join(os.path.dirname(__file__), 'wells.json')
    with open(json_path, 'r') as file:
        wells = json.load(file)
    return wells