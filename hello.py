from flask import Flask #import the Flask class from the flask module

app = Flask(__name__)#create an instance of the Flask class

@app.route("/") #python decorator
def index(): #function that returns a string
    return "Hello, World!" #return a string


app.run(host="0.0.0.0", port=80) #run the app
