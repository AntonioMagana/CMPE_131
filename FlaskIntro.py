#include flask class from package Flask
from flask import Flask

#create an instance of Flask class
app = Flask(__name__)

#different url the app will implement
@app.route("/")

#called view function
def hello():
    return "Hello World!"

#set up web server
app.run()
