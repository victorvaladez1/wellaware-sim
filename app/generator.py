import random
import datetime
import json
import os

def generate_sensor_reading(well_id):
    pressure = round(random.uniform(100, 250), 2)
    temperature = round(random.uniform(70, 120), 2)
    flow_rate = round(random.uniform(20, 50), 2)

    if pressure > 230:
        status = "HIGH PRESSURE"
    elif flow_rate < 25:
        status = "LOW FLOW"
    elif temperature > 115:
        status = "HIGH TEMP"
    else:
        status = "NORMAL"

    return {
        "well_id": well_id,
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "pressure": pressure,
        "temperature": temperature,
        "flow_rate": flow_rate,
        "status": status
    }

def get_all_wells():
    json_path = os.path.join(os.path.dirname(__file__), 'wells.json')
    with open(json_path, 'r') as file:
        return json.load(file)
