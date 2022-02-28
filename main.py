from os import listdir

from flask import Flask, render_template, request, redirect, url_for

from loginform import LoginForm

app = Flask(__name__)

STATIC_PATH = 'static'
TEMPLATE_PATH = 'templates'
USER_IMAGE_PATH = 'static/img/user_images'
LIST_OF_DIRS = list(map(lambda x: x.split('.')[0], listdir('templates')))
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

LIST_OF_DIRS.pop(LIST_OF_DIRS.index('antiignoregit'))

def return_links():
    return LIST_OF_DIRS


def return_images():
    return list(map(lambda x: f'{USER_IMAGE_PATH}/{x}', listdir(USER_IMAGE_PATH)))


@app.route('/')
@app.route('/base')
@app.route('/index/<title>')
def index(title='Главная страница'):
    params = {
        'title': title,
        'navbar_title': 'Миссия Колонизация Марса',
        'hrefs': return_links()
    }
    return render_template('base.html', **params)


@app.route('/training/')
@app.route('/training/<prof>')
def training(prof="врач"):
    prof = prof.lower().split()
    params = {
        'title': 'Тренировка',
        'navbar_title': 'Миссия Колонизация Марса',
        'prof': prof,
        'hrefs': return_links()
    }
    return render_template('training.html', **params)


@app.route('/list_prof/')
@app.route('/list_prof/<list_type>')
def list_prof(list_type="ul"):
    if list_type not in ["ul", "ol"]:
        list_type = "ul"
    params = {
        'title': 'Лист с профессиями',
        'navbar_title': 'Миссия Колонизация Марса',
        'list_type': list_type,
        'prof_list': ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолон', 'врач',
                      'инжинер по терраформированию', 'климатоллог'],
        'hrefs': return_links()
    }
    return render_template('list_prof.html', **params)


@app.route('/answer/')
@app.route('/auto_answer/')
def answer():
    params = {
        'title': 'Ответ',
        'navbar_title': 'Миссия Колонизация Марса',
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": "True",
        'hrefs': return_links()

    }
    return render_template('answer.html', **params)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    params = {
        'title': 'Логин',
        'navbar_title': 'Миссия Колонизация Марса',
        'hrefs': return_links()
    }
    if form.validate_on_submit():
        for key in request.form.keys():
            print(key, '-', request.form[key])
        return "<h1>Валидация прошла успешно!</h1>"
    return render_template('login.html', **params, form=form)


@app.route('/distribution')
def distribution():
    params = {
        'title': 'Логин',
        'navbar_title': 'Миссия Колонизация Марса',
        'hrefs': return_links(),
        'list_of_ast': ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    }
    return render_template('distribution.html', **params)


@app.route('/gallery', methods=['POST', 'GET'])
def gallery():
    params = {
        'title': 'Галлерея',
        'navbar_title': 'Миссия Колонизация Марса',
        'hrefs': return_links(),
        'images': return_images()
    }
    if request.method == 'POST':
        f = request.files['file']
        file_img = f'{USER_IMAGE_PATH}/image_{len(params["images"]) + 1}.png'
        with open(file_img, "wb") as file:
            file.write(f.read())
        return redirect(url_for("gallery"))
    return render_template('gallery.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
