import os

from flask import Flask, render_template

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/", methods=["GET", "POST"])

def index():

        return render_template("index.html")


