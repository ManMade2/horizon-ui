from flask import Blueprint, render_template, request, jsonify

from horizon_ui.schemas import all, getButton, getNav, getAlert, getInput
from horizon_ui.requests import deserialize, serializeComponent


endpoints = Blueprint(
    "ui_library", __name__, template_folder="templates", static_folder="static"
)


@endpoints.route("/getSchema", methods=["GET"])
def get_schema():

    return jsonify(all)


@endpoints.route("/getButton", methods=["POST"])
def create_button():

    data = request.get_data()
    if not data:
        return jsonify({"error": "No data received"}), 400

    req = deserialize(data, getButton)
    component = render_template("button.html", data=req)

    return serializeComponent(component)


@endpoints.route("/getNav", methods=["POST"])
def create_nav():

    data = request.get_data()
    if not data:
        return jsonify({"error": "No data received"}), 400

    req = deserialize(data, getNav)
    component = render_template("nav.html", data=req)

    return serializeComponent(component)


@endpoints.route("/getAlert", methods=["POST"])
def create_alert():

    data = request.get_data()
    if not data:
        return jsonify({"error": "No data received"}), 400

    req = deserialize(data, getAlert)
    component = render_template("alert.html", data=req)

    return serializeComponent(component)


@endpoints.route("/getInput", methods=["POST"])
def create_input():

    data = request.get_data()
    if not data:
        return jsonify({"error": "No data received"}), 400

    req = deserialize(data, getInput)
    component = render_template("input.html", data=req)

    return serializeComponent(component)


@endpoints.route("/getRadio", methods=["GET"])
def create_radio():

    req = {"id": "asdo", "text": "ues"}

    return render_template("radio.html", data=req)

    data = request.get_data()
    if not data:
        return jsonify({"error": "No data received"}), 400

    req = deserialize(data, getInput)
    component = render_template("input.html", data=req)

    return serializeComponent(component)
