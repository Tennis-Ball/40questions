from app import app
from flask import render_template, request, flash


@app.route("/test", methods=["GET"])
def home():
    return render_template("test.html.j2")

