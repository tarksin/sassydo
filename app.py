from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

app.config['DEBUG']= False
app.config['SECRET_KEY'] = 'ddd91417-11fa-40b5-98c1-fde58db3086d'

@app.route('/')
def index():
    return  render_template('necklaces.html')

@app.route('/necklaces')
def necklaces():
    return  render_template('necklaces.html')


@app.route('/lark')
def day():
    return  render_template('lark.html')


@app.route('/bp')
def bp():
    return  render_template('bp.html')

