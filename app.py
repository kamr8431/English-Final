from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/interview")
def interview():
    return render_template("interview.html")

@app.route("/dream")
def dream():
    return render_template("dream.html")

@app.route("/immigrant")
def immigrant():
    return render_template("immigrant.html")

if __name__ == "__main__":
    app.run(debug=True)