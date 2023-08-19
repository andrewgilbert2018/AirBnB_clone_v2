#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
    /python/(<text>): Displays 'Python' followed by the value of <text>.
    /number/<n>: Displays 'n is a number' only if <n> is an integer.
    /number_template/<n>: Displays an HTML page only if <n> is an integer.
        - Displays the value of <n> in the body.
    /number_odd_or_even/<n>: Displays an HTML page only if <n> is an integer.
        - States whether <n> is even or odd in the body.
"""
"""
Starts a server
"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<string:name>')
def cname(name=None):
    name = name.replace("_", " ")
    return "C {}".format(name)


@app.route('/python/', defaults={'text': "is cool"})
@app.route('/python/<string:text>')
def pythontext(text="is cool"):
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:num>')
def isnumber(num=None):
    return "{} is a number".format(num)


@app.route('/number_template/<int:num>')
def return_page(num=None):
    return render_template("5-number.html", value=num)


@app.route('/number_odd_or_even/<int:num>')
def return_page_even(num=None):
    if (num & 1):
        data = "{} is odd".format(num)
        return render_template("6-number_odd_or_even.html", value=data)
    else:
        data = "{} is even".format(num)
        return render_template("6-number_odd_or_even.html", value=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
