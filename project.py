from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'contact': u'9892914008',
        'name': u'Deepti Gupta', 
        'done': False
    },
    {
        'id': 2,
        'contact': u'8097940597',
        'name': u'Atharva Gupta', 
        'done': False
    }
]

# Now define a small route 
@app.route("/hello")
def hello_world():
    return "Hello World"

@app.route("/add-data", methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": 'error',
            "message": "Please provide the data"
        })

    task = {
        'id': tasks[-1]['id'] + 1,
        'contact': request.json.get('contact', ""),
        'name': request.json.get('name', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status": 'success',
        "message": "Task added successfully"
    })

@app.route("/get-data", methods = ["GET"])
def get_task():
    return jsonify({
        "data": tasks
    })

if (__name__ == '__main__'): 
    app.run()