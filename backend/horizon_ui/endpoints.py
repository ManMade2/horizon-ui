from flask import Blueprint, render_template, request, Response, jsonify


endpoints = Blueprint(
    "ui_library", __name__, template_folder="templates", static_folder="static"
)


@endpoints.route("/getButton", methods=["POST"])
def create_button():

    return Response()
