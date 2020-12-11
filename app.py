from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Esta es una prueba de como se hace deploy de una app Flask en Heroku'

if __name__ == '__main__':
    app.run()