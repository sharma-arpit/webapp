from flask import Flask, render_template, session, url_for
from app import app
from werkzeug.utils import redirect

queue = app.config['queue']


@app.route("/", methods=["GET"])
def index():
    print("******INDEX******")

    print("Opening Index page.")
    return render_template('index.html')

@app.route("/process", methods=["GET"])
def process():

    job = queue.enqueue('app.tasks.example', 23)
    return str(job.get_id())

