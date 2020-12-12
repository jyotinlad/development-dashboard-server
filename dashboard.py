from argparse import ArgumentParser
from datetime import datetime
from flask import Flask, jsonify, request
from json import load
from os import path
from pathlib import Path
from waitress import serve

from boardstats import BoardStats
from listing import Listing


app = Flask(__name__)


@app.errorhandler(400)
def invalid_query(message):
    return f"<h1>400</h1><p>{message}</p>", 400


def get_progress_config():
    file = path.join(Path(__file__).parent.absolute(), "config.json")
    with open(file, "r") as fh:
        return load(fh)


def get_progress_data(interval):
    data = []

    config = get_progress_config()
    for board_id in config.get("boards"):
        records = []

        stat = getattr(BoardStats, interval)(board_id)
        summary = stat.get("records")
        for date in sorted(list(summary.keys())):
            records.append({
                "x": date.strftime("%Y-%m-%d"),
                "y": summary.get(date, 0)
            })

        data.append({
            "id": stat.get("name"),
            "data": records
        })
    
    return data


@app.route("/", methods=["GET"])
def home():
    return "Development Dashboard Home"


@app.route("/api/v1/dashboard/listing", methods=["GET"])
def listing():
    query_parameters = request.args
    parameters = ["type"]
    for parameter in parameters:
        if parameter not in query_parameters:
            return invalid_query(f"Missing Parameter: {parameter}")
    
    return jsonify(Listing.get(query_parameters.get("type")))


@app.route("/api/v1/dashboard/progress", methods=["GET"])
def progress():
    query_parameters = request.args
    if 'interval' not in query_parameters:
        return invalid_query("Missing Parameter: interval")
    
    interval = query_parameters.get("interval")
    intervals = ["monthly", "quarterly"]
    if interval not in intervals:
        return invalid_query(f"Invalid Parameter Value: interval requires one of {intervals}")

    return jsonify(get_progress_data(interval))


if __name__ == "__main__":
    parser = ArgumentParser(description="Launch Dashboard API Service")
    parser.add_argument("--debug", action="store_true", help="Debug Mode")
    args = parser.parse_args()

    debug = args.debug
    mode = "DEBUG" if debug else "LIVE"

    if debug:
        app.config["DEBUG"] = debug
        app.run()
    else:
        serve(app, host="0.0.0.0", port=2800)
