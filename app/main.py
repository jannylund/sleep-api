import time

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'ok'

@app.route('/sleep/<int:seconds>')
def sleep_r(seconds):
    time.sleep(seconds)
    return "ok (delayed {} seconds)".format(seconds)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
