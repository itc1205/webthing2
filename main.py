from flask import Flask, render_template, url_for

app = Flask(__name__)

STATIC_PATH = 'static'
TEMPLATE_PATH = 'templates'


@app.route('/')
@app.route('/index/<title>')
def index(title='Main_page'):
    params = {
        'title': title,
        'navbar_title': 'Миссия Колонизация Марса'
    }
    return render_template('base.html', **params)


@app.route('/training/')
@app.route('/training/<prof>')
def training(prof="врач"):
    prof = prof.lower().split()
    params = {
        'title': 'zero_title',
        'navbar_title': 'Миссия Колонизация Марса',
        'prof': prof
    }
    print(url_for(STATIC_PATH, filename='img/sci.png'))
    return render_template('training.html', **params)


@app.route('/list_prof/')
@app.route('/list_prof/<list_type>')
def list_prof(list_type="ul"):
    if list_type not in ["ul", "ol"]:
        list_type = "ul"
    params = {
        'title': 'zero_title',
        'navbar_title': 'Миссия Колонизация Марса',
        'list_type': list_type,
        'prof_list': ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолон', 'врач',
                      'инжинер по терраформированию', 'климатоллог']
    }
    return render_template('list_prof.html', **params)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    params = {
        'title': 'zero_title',
        'navbar_title': 'Миссия Колонизация Марса',
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": "True"

    }
    return render_template('answer.html', **params)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
