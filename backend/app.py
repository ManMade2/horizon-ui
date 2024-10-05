from flask import Flask
from flask_cors import CORS

from horizon_ui import endpoint

app = Flask(__name__)
CORS(app, origins="http://127.0.0.1:5500")

app.register_blueprint(endpoint, url_prefix="/api/v1/components")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
