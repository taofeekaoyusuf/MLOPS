from flask import Flask, jsonify, request  # Import Flask Package

# Flask Application Initialization
# - This operation creates an instance of Flask Class which is the WSGI Application
app=Flask(__name__)

items = [
    {"id": 1, "name": "Item 1", "description": "This contains Item 1 stuffs"},
    {"id": 2, "name": "Item 2", "description": "This contains Item 2 stuffs"}
]

# Route / Web Page Creation
@app.route("/")
def welcome():
    return "Bismillaah Ar-Rahmani Ar-Roheem ....Welcome to My TODO List App"

# Route / Web Page Creation
@app.route("/index")
def index():
    return "Dfortunate Incorporation"

# GET ITEMS: Retrieving all the ITEMS
@app.route('/items', methods=['GET'])
def get_items():
    # item = item for item in items
    return jsonify(items)

# GET ITEM BY ID
@app.route('/items/<int:item_id>', method=['GET'])
def get_item(item_id):
    item=next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"ERROR": "ITEM NOT WANIBE"})
    return jsonify(item)

# POST REQUEST: CREATING A NEW TODO TASK
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({"ERROR": "ITEM NOT FOUND"})
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json['description']
    }
    items.append(new_item)
    return jsonify(items)

# PUT a.k.a. UPDATING AN EXISTING ITEM
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item=next((item for item in items if item['id'] == item_id), None) # Retrieve item from the list
    if item is None:
        return jsonify({"ERROR": "ITEM NOT FOUND"})
    item['name'] = request.json.get('name', item['name'])
    item['description'] =  request.json('description', item['description'])

    return jsonify(item)

# DELETE: Permanent removing a task from the TODO List
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] == item_id]
    return jsonify({"RESULT": "ITEM HAS BEEN DELETED"})

# App Execution starts here
if __name__ == "__main__":
    app.run(debug=True)
