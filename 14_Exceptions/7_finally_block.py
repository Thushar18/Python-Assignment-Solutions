def divide_numbers(a,b):
    try:
        result = a / b
        print("Result:",result)
    
    except ZeroDivisionError:
        print("Error:Cannot divide by zero")
    
    finally:
        print("Finally block: This block always executes")

def main():
    print("Case 1: Division with valid numbers")
    divide_numbers(18,3)

    print("Case 2: Division by zero (exception will occur)")
    divide_numbers(7,0)

main()