from flask import Flask, jsonify
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)

# MongoDB Atlas connection string
# Replace <username>, <password>, and <cluster-url> with your MongoDB Atlas credentials
mongo_uri = "mongodb+srv://atharvp540:w4oWEYdADEznQT4T@clustertest.ryyqg.mongodb.net/?retryWrites=true&w=majority&appName=ClusterTest"

# Create a MongoClient instance
client = MongoClient(mongo_uri)

# Select the database
db = client['Campus-placement-system']

# Select the collection
collection = db['Login']

@app.route('/')
def home():
    return "Welcome to the Flask MongoDB Atlas Connection!"

@app.route('/data')
def get_data():
    # Fetch data from the collection
    data = collection.find()
    # Convert the data to JSON and return it
    return dumps(data)

if __name__ == '__main__':
    app.run(debug=True)