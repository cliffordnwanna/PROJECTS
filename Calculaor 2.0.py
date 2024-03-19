# Calculator 2.0.py 
import math

class Calculator:
    def __init__(self):
        # Initialize the dictionary with basic mathematical operations and functions
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide,}

    def add_operation(self, symbol, function):
        # Add a new operation and its corresponding function to the dictionary
        self.operations[symbol] = function

    def calculate(self, num1, operator, num2):
        # Check if the operator is valid
        if operator not in self.operations:
            print("Invalid operator.")
            return None

        # Check if the input values are numbers
        if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
            print("Invalid input. Both inputs must be numbers.")
            return None

        # Perform the calculation using the corresponding function
        try:
            result = self.operations[operator](num1, num2)
            return result
        except ZeroDivisionError:
            print("Error: Division by zero.")
            return None

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError
        return num1 / num2

    # Add advanced mathematical operations to the calculator
    def add_advanced_operations(self):
        self.add_operation('^', self.exponentiation)
        self.add_operation('sqrt', self.square_root)
        self.add_operation('log', self.logarithm)

    def exponentiation(self, num1, num2):
        return num1 ** num2

    def square_root(self, num1, num2):
        if num1 < 0:
            print("Error: Cannot calculate square root of a negative number.")
            return None
        return math.sqrt(num1)

    def logarithm(self, num1, num2):
        if num1 <= 0 or num2 <= 0:
            print("Error: Cannot calculate logarithm with non-positive numbers.")
            return None
        return math.log(num1, num2)

# Create an instance of the Calculator class
calculator = Calculator()
calculator.add_advanced_operations()

# Main program
while True:
    print("Available operations: +, -, *, /, ^ (exponentiation), sqrt (square root), log (logarithm)")
    num1 = input("Enter the first number: ")
    if num1 == 'exit':
        break
    operator = input("Enter the operation symbol: ")
    num2 = input("Enter the second number: ")

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    result = calculator.calculate(num1, operator, num2)
    if result is not None:
        print(f"Result: {result}")