from flask import Flask, render_template

app = Flask(_name_)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/membership")
def membership():
    return render_template("membership.html")

if _name_=="main":
    app.run(debug=True)