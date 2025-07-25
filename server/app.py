from flask import Flask, send_from_directory, request
import os

app = Flask(__name__, static_folder="../web", static_url_path="")

@app.route("/")
def index():
    return send_from_directory("../web", "index.html")

@app.route("/api/user")
def get_user():
    uid = request.args.get("uid")
    return { "uid": uid, "balance": 100 }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
