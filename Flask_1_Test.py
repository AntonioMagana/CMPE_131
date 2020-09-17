from flask import Flask

app = Flask(__name__)

@app.route("/")

def hell():
    print("Hello World")

app.run()
