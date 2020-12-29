from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h3>sassydo index()</h3>'


@app.route('/necklaces')
def necklaces():
    return '<h3>sassydo necklaces()</h3>'