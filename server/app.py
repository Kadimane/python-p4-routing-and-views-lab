from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'
@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter
@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join(str(num) for num in range(parameter))
    numbers += '\n'  # Add a trailing newline character
    return numbers
   





@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    if result is not None:
        return str(result)
    else:
        return 'Invalid operation'
    return str(result)




if __name__ == '__main__':
    app.run()


    


    
    

