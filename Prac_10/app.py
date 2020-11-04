from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World, How are you :>) </h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return 'Hello ' + name


if __name__ == '__main__':
    app.run()
