def divide(a,b):
    try:
        result = a / b
        print("Result is:",result)
    except ZeroDivisionError:
        print("Cannot divided by zero - Arithemetic Exception handled.")

def main():
    num1 = 18
    num2 = 0

    print("Attempting Division...")
    divide(num1,num2)

main()