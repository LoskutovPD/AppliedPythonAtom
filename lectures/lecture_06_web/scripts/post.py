import time
import uuid

from flask import Flask, abort, request, jsonify


# export FLASK_ENV=development
# export FLASK_APP=post.py
# flask run --host=127.0.0.1
app = Flask(__name__)

memory = {}


# Обработка POST запроса
@app.route('/auth', methods=['POST'])
def auth():
    content = request.json
    if not content:
        return abort(418)  # Я чайник

    # Валидация данных
    name, surname, age = content.get('name'), content.get('surname'), content.get('age')
    if not (name and surname and isinstance(age, int) or age >= 0):
        return abort(400)

    # Логгирование запроса
    app.logger.debug('Auth %s %s!', name, surname)

    token = str(uuid.uuid4())
    # Сохранение запроса
    memory[token] = {
        'name': name,
        'surname': surname,
        'age': age,
    }
    return jsonify({'token': token})


# Обработка POST запроса с параметром в URL
@app.route('/update/<token>', methods=['POST'])
def update(token):
    if token not in memory:
        abort(404)  # Не найдено

    content = request.json
    if not content:
        return abort(418)  # Я чайник

    # Валидация данных
    name, surname, age = content.get('name'), content.get('surname'), content.get('age')
    if name == '' or surname == '' or not isinstance(age, int) or age < 0:
        return abort(400)

    # Логгирование запроса
    app.logger.debug('Update %s %s!', memory[token]['name'], memory[token]['surname'])

    # Сохранение запроса
    for field, value in content.items():
        if field in memory[token]:
            memory[token][field] = value

    return '', 204  # Ответ без контента


# Обработка GET запроса с параметром в URL
@app.route('/info/<token>')
def info(token):
    if token not in memory:
        abort(404)
    return jsonify(memory[token])


# Обработка DELETE запроса с параметром в URL
@app.route('/delete/<token>', methods=['DELETE'])
def delete(token):
    if token not in memory:
        abort(404)
    del memory[token]
    return '', 204


# Обработка заголовка
@app.route('/admin/all_users')
def all_users():
    if request.headers.get('Secret-Word') != 'Dratuti':
        abort(403)

    return jsonify([user for user in memory.values()])


# Обработка заголовка
@app.route('/admin/all_tokens')
def all_tokens():
    if request.headers.get('Secret-Word') != 'Dratuti':
        abort(403)

    return jsonify(list(memory.keys()))


# DRY Проверяем заголовок только в одном месте
def check_admin(func):
    def wrapper(*args, **kwargs):
        if request.headers.get('Secret-Word') != 'Dratuti':
            abort(403)
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper


@app.route('/admin_wrap/all_users')
@check_admin
def all_users_wrap():
    return jsonify([user for user in memory.values()])


@app.route('/admin_wrap/all_tokens')
@check_admin
def all_tokens_wrap():
    return jsonify(list(memory.keys()))


def start_timer():
    request.start_time = time.time()


def stop_timer(response):
    total_time = (time.time() - request.start_time) * 1000
    response.headers['Http-Response-Time'] = total_time
    return response


def setup_metrics(app):
    app.before_request(start_timer)
    app.after_request(stop_timer)


# setup_metrics(app)
