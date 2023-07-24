from flask import Flask
from random import *

app = Flask(__name__)

number = randint(1, 9)

@app.route('/')
def home():
    return '<h1 style="text-align : center">Guess a number between 0 and 9</h1>' \
           '<p style="text-align:center;"><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width="500"></p>'

@app.route('/<guess>')
def check_number(guess):
    if int(guess) > number:
        return f'<h1>{guess} is too high. Try Again</h1>' \
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width="280">'
    elif int(guess) < number:
        return f'<h1>{guess} is too low. Try Again</h1>' \
                   '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width="300">'
    else:
        return f'<h1>You found me!</h1>' \
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width="300">'



if __name__ == "__main__":
    app.run(debug=True)