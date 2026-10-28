#!/usr/bin/env python3
"""task 04 flask"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "<p>Welcome to the Flask API!</p>"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_username(username):
    try:
        user = users[username]
        return jsonify(user)
    except KeyError:
        return jsonify({"error": "User not found"}), 404


@app.post("/add_user")
def add_user():
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    if data["username"] in users:
        return jsonify({"error": "Username already exists"}), 409

    users[data["username"]] = data
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    app.run()