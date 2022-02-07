from flask import Flask, render_template

app = Flask(__name__)

STATIC_PATH = 'static'
TEMPLATE_PATH = 'templates'


@app.route('/')
@app.route('/index')
def index():
    params = {
        'title': 'Main page'
    }
    return render_template('index.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
