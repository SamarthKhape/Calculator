import math

def advanced_calculator():
    print("Advanced Python Calculator")
    print("Supported operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (**)")
    print("6. Modulus (%)")
    print("7. Floor Division (//)")
    print("8. Square Root (sqrt)")
    print("9. Logarithm (log)")
    print("10. Sine (sin)")
    print("11. Cosine (cos)")
    print("12. Tangent (tan)")
    print("13. Enter full expression")
    print("0. Exit")

    while True:
        choice = input("\nEnter your choice (0-13): ")

        if choice == '0':
            print("Exiting calculator.")
            break

        if choice in ['1','2','3','4','5','6','7']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1':
                    result = num1 + num2
                elif choice == '2':
                    result = num1 - num2
                elif choice == '3':
                    result = num1 * num2
                elif choice == '4':
                    if num2 == 0:
                        print("Error: Division by zero is not allowed.")
                        continue
                    result = num1 / num2
                elif choice == '5':
                    result = num1 ** num2
                elif choice == '6':
                    result = num1 % num2
                elif choice == '7':
                    if num2 == 0:
                        print("Error: Division by zero is not allowed.")
                        continue
                    result = num1 // num2
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice in ['8','9','10','11','12']:
            try:
                num = float(input("Enter number: "))
                if choice == '8':
                    if num < 0:
                        print("Error: Cannot compute square root of negative number.")
                        continue
                    result = math.sqrt(num)
                elif choice == '9':
                    if num <= 0:
                        print("Error: Logarithm undefined for zero or negative numbers.")
                        continue
                    result = math.log(num)
                elif choice == '10':
                    result = math.sin(math.radians(num))
                elif choice == '11':
                    result = math.cos(math.radians(num))
                elif choice == '12':
                    result = math.tan(math.radians(num))
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '13':
            expr = input("Enter the expression to evaluate: ")
            try:
                # Safe evaluation of expression
                allowed_names = {
                    'sqrt': math.sqrt,
                    'log': math.log,
                    'sin': lambda x: math.sin(math.radians(x)),
                    'cos': lambda x: math.cos(math.radians(x)),
                    'tan': lambda x: math.tan(math.radians(x)),
                    'pow': pow,
                    'abs': abs,
                    'round': round,
                    'math': math
                }
                code = compile(expr, "<string>", "eval")
                for name in code.co_names:
                    if name not in allowed_names:
                        raise NameError(f"Use of '{name}' not allowed")
                result = eval(code, {"__builtins__": {}}, allowed_names)
                print(f"Result: {result}")
            except Exception as e:
                print(f"Error evaluating expression: {e}")

        else:
            print("Invalid choice. Please enter a number between 0 and 13.")

if __name__ == "__main__":
    advanced_calculator()