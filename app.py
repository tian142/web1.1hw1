
from flask import Flask
from random import randint, choice

import random

app = Flask(__name__)


@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'


@app.route('/penguins')
def turtles_page():
    return "Penguins are cute!"


@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'


@app.route('/dessert/<users_dessert>')
def fav_desert(users_dessert):
    return f'How did you know I liked {users_dessert}?'


@app.route('/madlibs/<adjective>/<noun>')
def sentence(adjective, noun):
    return f'The {adjective} {noun} is no longer {adjective} because it is late in the day'


@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if number1.isdigit() and number2.isdigit():
        product = int(number1) * int(number2)
        return f'{number1} times {number2} is {product}.'
    else:
        return 'Invalid inputs. Please try again by entering 2 numbers!'


@app.route('/sayntimes/<word>/<n>')
def ntimes(word, n):
    return ((word + ' ') * int(n))


@app.route('/reverse/<word>')
def reverse(word):
    return word[::-1]


@app.route('/strangecaps/<word>')
def strange(word):
    newword = ''
    for letter in word:
        rand = random.randint(0, 1)
        if rand == 0:
            newword += letter.upper()
        else:
            newword += letter.lower()
    return word


if __name__ == '__main__':
    app.run(debug=True)
