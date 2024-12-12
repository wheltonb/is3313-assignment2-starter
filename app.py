from flask import Flask, render_template, request
from calculator import Calculator

app = Flask(__name__)
math_ops = Calculator()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]

        try:
            if operation == "add":
                result = math_ops.add(num1, num2)
            elif operation == "subtract":
                result = math_ops.subtract(num1, num2)
            elif operation == "multiply":
                result = math_ops.multiply(num1, num2)
            elif operation == "divide":
                result = math_ops.divide(num1, num2)
            elif operation == "power":
                result = math_ops.power(num1, num2)
            elif operation == "modulus":
                result = math_ops.modulus(num1, num2)
        except ValueError as e:
            result = str(e)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
