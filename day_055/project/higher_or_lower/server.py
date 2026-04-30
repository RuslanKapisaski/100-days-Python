from flask import Flask
from random import randint

app = Flask(__name__)

RANDOM_NUMBER = randint(1, 9)

@app.route('/')
def home_page():
    return ('<div style="text-align: center; justify-content: center">  '
            '<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzU2ZG0zcTF5NGl3bXIwc2VseHhnMWd1cnFjYW5jcmtyZDh4cWRycyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tWhSt6azAiDYhW9VhG/giphy.gif" width=800/>'
            '</div>')

@app.route('/<int:number>')
def guess_number(number):
    if number > RANDOM_NUMBER:
        return ('<div style="text-align: center; justify-content: center">'
                '<h1 style="color: red">Too high!</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=600/>'
                '</div>')
    elif number < RANDOM_NUMBER:
        return ('<div style="text-align: center; justify-content: center">'
                '<h1 style="color: red">Too low!</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=600/>'
                '</div>')
    else:
        return ('<div style="text-align: center;justify-content: center">'
                '<h1 style="color: green">Correct!</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=600/>'
                '</div>')

if __name__ == '__main__':
    app.run(debug=True)