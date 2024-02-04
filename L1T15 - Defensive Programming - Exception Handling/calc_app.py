# Function to calculate the addition of two numbers.
def add(x, y):
    """Calculates the addition x + y.

    Keyword arguments:
    float -- first argument
    float -- second argument
    """
    total = x + y
    return (total)

# Function to calculate the subtraction of two numbers.
def subtract(x, y):
    """Calculates the subtraction x - y.

    Keyword arguments:
    float -- first argument
    float -- second argument
    """
    total = x - y
    return (total)

# Function to calculate the multiplication of two numbers.
def multiply(x, y):
    """Calculates the multiplication x * y.

    Keyword arguments:
    float -- first argument
    float -- second argument
    """
    total = x * y
    return (total)

# Function to calculate the division of two numbers, handles division by zero error.
def divide(x, y):
    """Calculates the division x / y.

    Keyword arguments:
    float -- first argument
    float -- second argument
    """
    try:
        total = x / y
        return(total)
    except ZeroDivisionError:
        raise ZeroDivisionError("Error: Division by zero is not allowed.")

# Function to perform the specified operation on two numbers.    
def perform_operation(num1, num2, operation):
    """Performs a given arithmetic operation (+, -, *, /) on two numbers.

    Arguments:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operator (+, -, *, /).

    Returns:
        float: The result of the operation.
    """
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)

# Function to get a valid numeric input from the user, handles ValueError.          
def get_number_input(input_message):
    while True:
        try:
            return float(input(input_message))
        except ValueError:
            print("Error: Please enter valid numbers.")

# Function to get a valid operation (+, -, *, /) from the user.
def get_operation():
     while True:
        operation = input("Enter the operation (+, -, *, /): ")
        valid_operations = ['+', '-', '*', '/']
        
        if not (operation in valid_operations):
            print("Invalid operation. Please enter +, -, *, or /.")
        else:
            return operation

# Function to perform a calculation based on user input and record the equation and result and saves the result to a file, handles ValueError.       
def perform_calculation():
    try:
        num1 = get_number_input("Enter the first number: ")
        num2 = get_number_input("Enter the second number: ")
        operation = get_operation()
        
        result = perform_operation(num1, num2, operation)

        equation = f"{num1} {operation} {num2} = {result}"
        print(f"Result: {equation}")

        with open('equations.txt', 'a+') as file:
            file.write(equation + '\n')

    except ValueError:
        print("Error: Please enter valid numbers.")
    except Exception as exception:
        print(f"An unexpected error occurred: {str(exception)}")

# Function to prints the equations stored in the 'equations.txt' file, or indicates if there are none (handles FileNotFoundError).
def print_previous_equations():
        try:
            with open('equations.txt', 'r') as file:
                equations = file.readlines()
                if len(equations) != 0:
                    print("Previous Equations:")
                    for equation in equations:
                        print(equation.strip())
                else:
                    print("No previous equations found.")
        except FileNotFoundError:
            print("No previous equations found.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

# Main program starts here.
def main():
    while True:
        print("\nCalculator Application")
        print("1. Perform Calculation")
        print("2. Print Previous Equations")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            perform_calculation()
        elif choice == '2':
            print_previous_equations()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()

