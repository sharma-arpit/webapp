from flask import Flask
from tempfile import gettempdir
from flask_session import Session
from redis import Redis
import rq


app = Flask(__name__, template_folder='templates')

if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-.cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-.cache"
        return response

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config['queue'] = rq.Queue('tasks', connection=Redis.from_url('redis://'))

from app import home