import random
import time

from flask import Flask

app = Flask(__name__)


def status(delay):
    return {
        "status": "ok",
        "delay": delay
    }


@app.route('/')
def index():
    return {"status": "ok"}


@app.route('/sleep/<int:seconds>', methods = ['GET', 'POST'])
def sleep(seconds):
    time.sleep(seconds)
    return status(seconds)


@app.route('/sleep/<int:min_seconds>/<int:max_seconds>', methods = ['GET', 'POST'])
def sleep_random(min_seconds, max_seconds):
    seconds = random.randint(min_seconds, max_seconds)
    time.sleep(seconds)
    return status(seconds)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
