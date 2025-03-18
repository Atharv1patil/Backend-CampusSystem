from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

# ✅ MongoDB Atlas connection string
mongo_uri = "mongodb+srv://atharvp540:w4oWEYdADEznQT4T@clustertest.ryyqg.mongodb.net/?retryWrites=true&w=majority&appName=ClusterTest"

# ✅ Create MongoDB Client
client = MongoClient(mongo_uri)

# ✅ Select Database and Collection
db = client['Campus-placement-system']
collection = db['Login']

# 🚀 **Home Route**
@app.route('/')
def home():
    return "Welcome to the Flask MongoDB Authentication System!"

# 🚀 **User Registration API**
@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user with hashed password."""
    
    try:
        # Get data from the request body
        data = request.json

        # Validate input fields
        if not all(k in data for k in ("username", "email", "password")):
            return jsonify({"error": "Missing username, email, or password"}), 400

        # Check if user already exists
        if collection.find_one({"email": data["email"]}):
            return jsonify({"error": "Email already registered"}), 409

        # Hash the password before storing
        hashed_password = bcrypt.generate_password_hash(data["password"]).decode('utf-8')

        # Insert user into MongoDB
        user_data = {
            "username": data["username"],
            "email": data["email"],
            "password": hashed_password  # Store hashed password
        }
        collection.insert_one(user_data)

        return jsonify({"message": "User registered successfully!"}), 201
    
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

# 🔐 **User Login API**
@app.route('/login', methods=['POST'])
def login_user():
    """Authenticate and validate user login."""
    
    try:
        # Get data from the request body
        data = request.json

        # Validate input fields
        if not all(k in data for k in ("email", "password")):
            return jsonify({"error": "Missing email or password"}), 400

        # Find the user in MongoDB
        user = collection.find_one({"email": data["email"]})

        # If user is not found
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Verify the password
        if bcrypt.check_password_hash(user["password"], data["password"]):
            return jsonify({
                "message": "Login successful!",
                "username": user["username"],
                "email": user["email"]
            }), 200
        else:
            return jsonify({"error": "Invalid password"}), 401

    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

# 🚀 **Run the Flask Application**
if __name__ == '__main__':
    app.run(debug=True)
