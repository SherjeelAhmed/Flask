from flask import Flask,request
import tensorflow
from tensorflow import keras
m = tensorflow.keras.models.load_model('/Users/Sherjeel Ahmed/PIAIC/Quarter-2/Deep Learning/Height_Weight.h5')

app = Flask(__name__)

@app.route("/")
def index():
    return'''
    <h1>Regression Problem<h1>
    <form action="/info" method="POST">
    <input type=text name="height" placeholder="Enter Height">
    <input type="submit" value="Send">
    </form>
    '''
@app.route("/info", methods=["GET","POST"])
def info():
    if request.method == "GET":
        result = m.predict([[float(request.args.get('height'))]])
        return "GET Method:<br>Height: {}<br>Weight: {}".format(request.args.get('height'),result)
    
    elif request.method == "POST":
        result = m.predict([[float(request.form['height'])]])
        return "POST Method:<br>Height: {}<br>Weight: {}".format(request.form['height'],result)

app.run(debug=True)