from flask import Blueprint, render_template, request, jsonify

from horizon_ui.schemas import all, getButton
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
