from flask import Flask
from random import randint

from project.calculator.calculator import Calculator


app = Flask(__name__)
my_calculator = Calculator()

@app.route("/")
def hello():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    return "{}, {}, {}".format(num1, num2, my_calculator.add(num1, num2))

if __name__ == "__main__":
    app.run()