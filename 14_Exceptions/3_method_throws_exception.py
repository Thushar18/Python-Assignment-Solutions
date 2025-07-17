def risky_operation():
    print("Inside risky operation")
    raise ValueError("This is manually raised exception!")

def main():
    print("starting program..")
    risky_operation()
    print("This line will not be executed due to exception.")

main()