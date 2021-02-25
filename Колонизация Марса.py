from flask import Flask, url_for

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
