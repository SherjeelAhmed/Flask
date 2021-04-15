from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    students=[
        {'id':1,'name':'Ali'},
        {'id':2,'name':'Umer'},
        {'id':3,'name':'Hassan'}
        ]
    return jsonify({'piaic_students':students})

app.run(debug=True)