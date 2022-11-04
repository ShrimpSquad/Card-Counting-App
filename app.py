from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home", methods = ["GET", "POST"])
def home():
    return render_template("home.html", myvar = "Seb")
if __name__ == "__main__":
    app.run(debug = True)