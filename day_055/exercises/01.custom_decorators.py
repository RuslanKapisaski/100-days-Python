import functools

from flask import Flask

app = Flask(__name__)

def bold_decorator(func):
    @functools.wraps(func)
    def bold_text():
        return f"<b>{func()}</b>"
    return bold_text

def italic_decorator(func):
    @functools.wraps(func)
    def make_italic_text():
        return f"<i>{func()}</i>"
    return make_italic_text

@app.route('/')
@bold_decorator
def greet():
    return '<h1>Hello World!</h1>'

@app.route('/bye')
@italic_decorator
@bold_decorator
def bye():
    return 'Bye!'


if __name__ == '__main__':
    app.run(debug=True)