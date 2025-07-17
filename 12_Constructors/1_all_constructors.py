class MyClass:
    def __init__(self,arg1=None,arg2=None):
        if arg1 is None and arg2 is None:
            print("Default Constructor is called:")
        elif arg2 is None:
            print(f"One-Argument Constructor called with value: {arg1}")
        else:
            print(f"Two-Argument Constructor called with values: {arg1},{arg2}")

def main():
    print("Creating obj1 with Default Constructor:")
    obj1 = MyClass()

    print("\n Creating obj2 with One-Argument Constructor:")
    obj2 = MyClass(100)
    
    print("\n Creating obj3 with Two-Argument Constructor:")
    obj3 = MyClass(100,200)

main()

