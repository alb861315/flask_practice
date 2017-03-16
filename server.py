from flask import Flask, request, render_template
from random import choice, randint


app = Flask(__name__)
COMPLIMENTS = ['awesome', 'great', 'smart']


@app.route('/')
def index():
    return "<html><body><h1>I am the landing page</h1></body></html>"


@app.route('/hello')
def say_hello():
    return "<html><body><h1>Hello</h1></body></html>"


@app.route('/lucky')
def lucky_number():
    lucky_num = randint(1, 10)
    return render_template('lucky.html', number=lucky_num)


@app.route('/form')
def show_form():
    return render_template('form.html')

@app.route('/greet')
def offer_greeting():
    person= request.args.get('person')
    nice_thing= choice(COMPLIMENTS)
    return render_template('compliment.html', name=person, compliment= nice_thing)

if __name__ == "__main__":
    app.run(debug=True)
