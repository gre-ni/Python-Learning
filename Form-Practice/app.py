from flask import Flask, render_template, request

app = Flask(__name__)

SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee",
    "Ballet",
]

@app.route("/")
def index():
	return render_template("index.html", sports=SPORTS)
	
@app.route("/register", methods=["POST"])
def register():

    # Validate name
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing name")
    
    # Validate sport
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing sport")
    elif sport not in SPORTS:
        return render_template("error.html", message="Sport unavailable")

    return render_template("success.html")