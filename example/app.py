import flask


Users=[]

app = flask.Flask(__name__)


@app.route('/')
def hello():
    print("happy")
    return flask.render_template("signup.html")

@app.route('/send',methods=["POST"])
def send():
    name= flask.request.form['namee']
    username= flask.request.form['username']
    email= flask.request.form['email']
    password= flask.request.form['password']


    for user in Users:
        if username in user:
            return "user already present"
    Users.append([username,[name,email,password]])
    return "user added"

@app.route('/users')
def showusers():
    return f"{Users}"
    


if __name__=="__main__":
    app.run(debug=True)
