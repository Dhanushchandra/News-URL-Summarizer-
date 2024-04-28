from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/TAS"
mongo = PyMongo(app)


@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    if "username" in data and "password" in data and "email" in data:
        username = data["username"]
        password = data["password"]
        email = data["email"]

        # Check if the email already exists
        existing_user = mongo.db.users.find_one({"email": email})
        if existing_user:
            return jsonify({"error": "Email already exists"}), 400

        # Hash the password before storing it in the database
        hashed_password = generate_password_hash(password)

        # Insert the new user data into MongoDB with hashed password
        user_data = {"username": username, "password": hashed_password, "email": email}
        mongo.db.users.insert_one(user_data)

        return jsonify({"message": "Signup successful", "username": username, "email": email}), 201
    else:
        return jsonify({"error": "Missing fields"}), 400


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if "email" in data and "password" in data:
        email = data["email"]
        password = data["password"]

        # Retrieve user data from the database based on the provided email
        user = mongo.db.users.find_one({"email": email})

        # Check if the user exists and the password is correct
        if user and check_password_hash(user["password"], password):
            return jsonify({"message": "Login successful", "username": user["username"], "email": user["email"]}), 200
        else:
            return jsonify({"error": "Invalid email or password"}), 401
    else:
        return jsonify({"error": "Missing email or password"}), 400


if __name__ == "__main__":
    app.run(port=5000, debug=True)
