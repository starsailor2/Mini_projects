from flask import Flask, request, jsonify

# initialize the Flask application
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API!"


#HTTP methods: GET, POST, PUT, DELETE
# GET is use to Request data from a specified resource.
# POST is used to create a new resource.
# PUT is used to update a current resource with new data.
# DELETE is used to delete a specified resource.

@app.route("/get-user/<user_id>")
def get_user(user_id):
    # In a real application, you would fetch user data from a database
    user_data = {
        'id': user_id,
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }

    extra = request.args.get("extra")
    if extra:
        user_data["address"] = "123 Main St, Anytown, USA"
        user_data["phone"] = "555-1234"

    return jsonify(user_data), 200 #default status code 200 means OK

# define a route for the API
@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {
        'id': 1,
        'name': 'Sample Item',
        'description': 'This is a sample item.'
    }
    return jsonify(sample_data)

@app.route("/create-user", methods=["POST", "PUT", "DELETE", "GET"])
def create_user():
    # if request.method == "POST":
        data = request.get_json()
        return jsonify(data), 201
        
if __name__ == "__main__":
    app.run(debug=True) #this will run the app in debug mode