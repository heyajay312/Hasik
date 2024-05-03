from flask import Flask, render_template, request

from helpers import get_event

app = Flask(__name__)


@app.route("/")
def index():
    year = request.args.get("year")
    month = request.args.get("month")
    day = request.args.get("day")
    output = get_event(year, month, day)

    return render_template("index.html", output=output)
