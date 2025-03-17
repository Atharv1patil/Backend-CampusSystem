from bson import ObjectId
# from flask import Flask, request, jsonify
# from flask_pymongo import PyMongo
#
# app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb+srv://atharvp540:w4oWEYdADEznQT4T@clustertest.ryyqg.mongodb.net/?retryWrites=true&w=majority&appName=ClusterTest"
# mongodb = PyMongo(app).db
#
#
# @app.route("/api/v1/todo", methods=["POST", "GET"])
# def fun():
#     if request.method == "GET":
#         todos = list(mongodb.Login.find({}, {"_id": 1, "name": 1, "College": 1,"Branch":1}))
#         for todo in todos:
#             todo["_id"] = str(todo["_id"])  # Convert ObjectId to string
#         return jsonify(todos)
#
#     elif request.method == "POST":
#         item = {"title": request.json['title'], "desc": request.json['desc']}
#         inserted_id = mongodb.todos.insert_one(item).inserted_id
#         item["_id"] = str(inserted_id)
#         return jsonify(item), 201
#
#
# # ✅ **UPDATE OR DELETE DATA**
# @app.route("/api/v1/update/<string:id>", methods=["PUT", "DELETE"])
# def fun1(id):
#     try:
#         mongodbid = ObjectId(id)  # Convert ID to ObjectId
#     except:
#         return jsonify({"error": "Invalid ObjectId format"}), 400
#
#     if request.method == "PUT":
#         data = request.json  # Get data from request
#         update_fields = {}
#
#         if "title" in data:
#             update_fields["title"] = data["title"]
#         if "desc" in data:
#             update_fields["desc"] = data["desc"]
#
#         # If no fields to update, return error
#         if not update_fields:
#             return jsonify({"error": "No valid fields to update"}), 400
#
#         # Perform update
#         result = mongodb.todos.update_one({"_id": mongodbid}, {"$set": update_fields})
#
#         if result.matched_count == 0:
#             return jsonify({"error": "Todo not found"}), 404
#
#         updated_todo = mongodb.todos.find_one({"_id": mongodbid}, {"_id": 1, "title": 1, "desc": 1})
#         updated_todo["_id"] = str(updated_todo["_id"])
#
#         return jsonify({"message": "Data updated successfully", "updated_data": updated_todo}), 200
#
#     elif request.method == "DELETE":
#         result = mongodb.todos.delete_one({"_id": mongodbid})
#
#         if result.deleted_count == 0:
#             return jsonify({"error": "Todo not found"}), 404
#
#         return jsonify({"message": "Todo deleted successfully"}), 200




# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

# Use environment variable for security
app.config["MONGO_URI"] = "mongodb+srv://atharvp540:<db_password>@clustertest.ryyqg.mongodb.net/?retryWrites=true&w=majority&appName=ClusterTest"
mongodb = PyMongo(app).db
print("db :",mongodb)


@app.route("/api/v1/todo", methods=["POST", "GET"])
def manage_todos():
    if request.method == "GET":
        todos = list(mongodb.Login.find({}, {"_id": 1, "name": 1, "College": 1, "Branch": 1}))
        for todo in todos:
            todo["_id"] = str(todo["_id"])  # Convert ObjectId to string
        return jsonify(todos), 200

    elif request.method == "POST":
        data = request.json
        if not data or "name" not in data:
            return jsonify({"error": "Missing required fields"}), 400

        inserted_id = mongodb.Login.insert_one(data).inserted_id
        return jsonify({"message": "Todo added", "id": str(inserted_id)}), 201


if __name__ == "__main__":
    app.run(debug=True)

