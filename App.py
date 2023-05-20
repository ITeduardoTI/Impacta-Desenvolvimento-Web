from flask import Flask, render_template

App = Flask(__name__)


@App.route('/')
def index():
    return "Olá mundo!"


@App.route('/saudacao')
def saudacao():
    return render_template('saudacao.html')


if __name__ == '__main__':
    App.run(debug=True)
