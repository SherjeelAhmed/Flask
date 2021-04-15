from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return " Hello World \
         New project"

@app.route("/about")
def about():
    return '''
    <h1> PIAIC ISLAMABAD  </h1>
    Latest state of the art technology
    '''

app.run(debug=True)