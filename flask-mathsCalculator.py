from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Math Operations API!"

@app.route('/math', methods=['GET', 'POST'])
def math_operations():
    if request.method == 'POST':
        data = request.get_json()
    else:
        data = request.args

    try:
        operation = data.get('operation')
        num1 = float(data.get('num1'))
        num2 = float(data.get('num2'))

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({'error': 'Division by zero is not allowed.'}), 400
            result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operation. Use add, subtract, multiply, or divide.'}), 400

        return jsonify({'operation': operation, 'num1': num1, 'num2': num2, 'result': result})

    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input. Please provide num1 and num2 as numbers.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
