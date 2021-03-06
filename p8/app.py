from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def index():
    return '''
    <h1>User Information</h1>
    <form action="/info" method="POST">
    <input type="text" name="user" placeholder="User Name">
    <input type="email" name="email" placeholder="Email Address">
    <input type="password" name="pass1" placeholder="Password">
    <input type="submit" value="Send">
    </form>
    ''' 
@app.route("/info",methods=["GET","POST"])
def info():
    if request.method == "GET":
        return "GET Method<br>User name: {}<br>Email: {}<br>Password:{}".format(request.args.get('user'),request.args.get('email'),request.args.get('pass1'))
    elif request.method == "POST":
        return  "POST Method<br>User name: {}<br>Email: {}<br>Password:{}".format(request.form['user'],request.form['email'],request.form['pass1'])

app.run(debug=True)