from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def title():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    countdown_list = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
                      "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!",
                      "Присоединяйся!", 'Пуск!']
    return '</br>'.join(countdown_list)


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
                        alt="здесь должна была быть картинка, но не нашлась">
                  </body>
                </html>"""

    # <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />


@app.route('/promotion_image')
def promotion_image():
    countdown_list = ["</br>Человечество вырастает из детства.", "Человечеству мала одна планета.",
                      "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!",
                      "Присоединяйся!", 'Пуск!']

    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />

                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
                        alt="здесь должна была быть картинка, но не нашлась"></br>
                    <div class="alert alert-success" role="alert">
                      {countdown_list[0]}
                    </div>
                    <div class="alert alert-danger" role="alert">
                      {countdown_list[1]}
                    </div>
                    <div class="alert alert-warning" role="alert">
                      {countdown_list[2]}
                    </div>
                    <div class="alert alert-info" role="alert">
                      {countdown_list[3]}
                    </div>
                    <div class="alert alert-light" role="alert">
                      {countdown_list[4]}
                    </div>
                    <div class="alert alert-dark" role="alert">
                      {countdown_list[5]}
                    </div>
                  </body>
                </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" 
                                href="{url_for('static', filename='css/styles_for_select.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="text" 
                                        placeholder="Введите вашу фамилию" name="text">
                                    <input type="text" class="form-control" 
                                        id="text" placeholder="Введите ваше имя" name="text">
                                    <input type="email" class="form-control" 
                                        id="email" placeholder="Введите вашу электронную почту" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>начальное</option>
                                          <option>среднее</option>
                                          <option>высшее</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="classSelect">Какие у вас есть професии?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>инженер-исследователь</option>
                                          <option>пилот</option>
                                          <option>строитель</option>
                                          <option>экзобиолог</option>
                                          <option>врач</option>
                                          <option>инженер по терраформированию</option> 
                                          <option>климатолог</option>
                                          <option>специалист по радиационной защите</option> 
                                          <option>астрогеолог</option>
                                          <option>гляциолог</option>
                                          <option>инженер жизнеобеспечения</option> 
                                          <option>метеоролог</option>
                                          <option>оператор марсохода</option> 
                                          <option>киберинженер</option>
                                          <option>штурман</option>
                                          <option>пилот дроно</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" 
                                                name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" 
                                                name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" 
                                            for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice_planet_name(planet_name):
    countdown_list = ["Эта планета близка к Земле", "На ней много необходимых ресурсов",
                      "На ней есть вода и атмосфера", "На ней есть небольшое магнитное поле",
                      "Наконец, она просто красива!"]

    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Моё предложение: {planet_name}</h1>
                    <div class="alert alert-success" role="alert">
                      {countdown_list[0]}
                    </div>
                    <div class="alert alert-danger" role="alert">
                      {countdown_list[1]}
                    </div>
                    <div class="alert alert-warning" role="alert">
                      {countdown_list[2]}
                    </div>
                    <div class="alert alert-info" role="alert">
                      {countdown_list[3]}
                    </div>
                    <div class="alert alert-light" role="alert">
                      {countdown_list[4]}
                    </div>
                  </body>
                </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претенденты на участии в миссии: {nickname}</h2>
                    <div class="alert alert-warning" role="alert">
                      Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                    <div class="alert alert-info" role="alert">
                      составляет {rating}!
                    </div>
                    <div class="alert alert-light" role="alert">
                      Желаем удчаи!
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
