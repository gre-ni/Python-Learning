from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # The only way to get there via post is to click the submit button
        return render_template("greet.html", name=request.form.get("name", "world"))
    else:
        # Get -> no form was submitted, so show form first
        return render_template("index.html")
