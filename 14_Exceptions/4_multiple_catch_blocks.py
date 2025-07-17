def process_operations():
    try:
        num = int(input("Enter a number:"))
        result = 10 / num

        text = input("Enter a string:")
        number = int(text)

        print("Computation Successful")
    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    
    except ValueError:
        print("Error:Invalid input. Could not convert to integer")
    
    except Exception as e:
        print(f"General Exception Caught: {e}")

def main():
    print("starting multiple exception handling")
    process_operations()

main()