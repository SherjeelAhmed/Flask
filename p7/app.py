from flask import Flask

app = Flask(__name__)

@app.route("/user/<name>")
def Index(name):
    return "Hello dear {}".format(name)

app.run(debug=True)