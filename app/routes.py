from flask import Blueprint, jsonify, request
from .generator import get_all_wells, generate_sensor_reading

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

@routes.route("/api/alerts", methods=["GET"])
def alerts():
    wells = get_all_wells()
    alerts = []

    for well in wells:
        reading = generate_sensor_reading(well["id"])
        if reading["status"] != ["NORMAL"]:
            alerts.append(reading)

    return jsonify(alerts)
