from datetime import datetime
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['POST'])
def index() -> any:
    date: datetime = datetime.now()
    assert request.method == 'POST'
    return f"Received at: {date.strftime('%H:%M:%S')}"
