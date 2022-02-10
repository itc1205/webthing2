from flask import Flask, render_template, url_for

app = Flask(__name__)

STATIC_PATH = 'static'
TEMPLATE_PATH = 'templates'


@app.route('/')
@app.route('/index/<title>')
def index(title='Main_page'):
    params = {
        'title': title,
        'navbar_title': 'Миссия Колонизация Марса '
    }
    return render_template('index.html', **params)


@app.route('/training/')
@app.route('/training/<prof>')
def training(prof="врач"):
    prof = prof.lower().split()
    params = {
        'title': 'Main page',
        'navbar_title': 'Миссия Колонизация Марса',
        'prof': prof
    }
    print(url_for(STATIC_PATH, filename='img/sci.png'))
    return render_template('training.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
