from flask import Flask, render_template #this imports from flask class to Python, allows the use of HTML files

app = Flask(__name__) #default flask environment

@app.route('/') #Page url 
def index():
    return "Homepage"


@app.route('/profile/<name>') #Page url 
def profile(name):
    return render_template("profile.html", name=name)


if __name__ == "__main__":  #if na
    app.run()

