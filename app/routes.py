from flask import Blueprint, jsonify, request
from .generator import get_all_wells, generate_sensor_reading

import os
import json

routes = Blueprint("routes", __name__)

@routes.route("/api/wells", methods=["GET"])
def wells():
    wells = get_all_wells()
    return jsonify(wells)

@routes.route("/api/readings", methods=["GET"])
def readings():
    wells = get_all_wells()

    well_id = request.args.get("well_id")
    if well_id:
        try:
            well_id = int(well_id)
            reading = generate_sensor_reading(well_id)
            return jsonify([reading])
        except ValueError:
            return jsonify({"error": "Invalid well_id"}), 400
        
    readings = [generate_sensor_reading(w["id"]) for w in wells]
    return jsonify(readings)

import os
import json

@routes.route("/api/alerts", methods=["GET"])
def alerts():
    wells = get_all_wells()
    alerts = []

    for well in wells:
        reading = generate_sensor_reading(well["id"])
        if reading["status"] != ["NORMAL"]:
            alerts.append(reading)

    if alerts:
        json_path = os.path.join(os.path.dirname(__file__), 'alerts.json')
        with open(json_path, 'r') as f:
            existing = json.load(f)

        existing.extend(alerts)

        with open(json_path, 'w') as f:
            json.dump(existing, f, indent=2)

    return jsonify(alerts)

@routes.route("/api/alert-log", methods=["GET"])
def alert_log():
    json_path = os.path.join(os.path.dirname(__file__), 'alerts.json')
    
    if not os.path.exists(json_path):
        return jsonify({"error": "alerts.json not found"}), 404

    with open(json_path, 'r') as f:
        data = json.load(f)

    return jsonify(data)

@routes.route("/api/wells", methods=["POST"])
def add_well():
    json_path = os.path.join(os.path.dirname(__file__), 'wells.json')

    # Load existing wells
    with open(json_path, 'r') as file:
        wells = json.load(file)

    # Get data from request
    data = request.get_json()
    name = data.get("name")
    location = data.get("location")

    if not name or not location:
        return jsonify({"error": "Missing name or location"}), 400

    # Assign new ID
    next_id = max(well["id"] for well in wells) + 1 if wells else 1
    new_well = {
        "id": next_id,
        "name": name,
        "location": location
    }

    # Add and save
    wells.append(new_well)
    with open(json_path, 'w') as file:
        json.dump(wells, file, indent=2)

    return jsonify(new_well), 201

@routes.route("/api/wells/<int:well_id>", methods=["DELETE"])
def delete_well(well_id):
    json_path = os.path.join(os.path.dirname(__file__), 'wells.json')

    # Load wells
    with open(json_path, 'r') as file:
        wells = json.load(file)

    # Look for well with matching ID
    updated_wells = [w for w in wells if w["id"] != well_id]

    if len(updated_wells) == len(wells):
        return jsonify({"error": f"Well with id {well_id} not found"}), 404

    # Save updated list
    with open(json_path, 'w') as file:
        json.dump(updated_wells, file, indent=2)

    return jsonify({"message": f"Well with id {well_id} deleted"}), 200

@routes.route("/api/alerts", methods=["DELETE"])
def clear_alerts():
    json_path = os.path.join(os.path.dirname(__file__), 'alerts.json')

    # Overwrite with empty list
    with open(json_path, 'w') as file:
        json.dump([], file, indent=2)

    return jsonify({"message": "All alerts cleared"}), 200

