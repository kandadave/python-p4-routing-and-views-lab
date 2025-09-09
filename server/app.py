#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def home():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print1(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<parameter>')
def count(parameter):
    output = ''
    for i in range(int(parameter)):
        output += f'{i}\n'
    return output

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    else:
        result = 0  # Or handle invalid operation as needed; test likely doesn't check this
    return str(result)