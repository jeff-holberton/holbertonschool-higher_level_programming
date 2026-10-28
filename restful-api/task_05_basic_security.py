#!/usr/bin/env python3
"""task 05 basic security"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "John",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "Jane",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@jwt.unauthorized_loader
def handle_missing_token(err):
    return 401


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users[username]["password"], password):
        return username


@app.route("/")
@auth.login_required
def home():
    return "Basic Auth: Access Granted"


@app.post("/login")
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user = users.get(username)
    if user is None or \
            check_password_hash(user["password"]) != password:
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=username)
    return jsonify({"access_token": token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required
def admin_only():
    current_user = get_jwt_identity()

    if users[current_user]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
