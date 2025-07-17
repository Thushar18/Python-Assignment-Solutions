class Parent:
    def __init__(self, value=None):
        if value is None:
            print("Parent Default Constructor called.")
        else:
            print(f"Parent Argument Constructor called with value:{value}")

class Child(Parent):
    def __init__(self,mode="default"):
        if mode == "default":
            print("Child Constructor is calling Parent Default Constructor")
            super().__init__()
        elif mode == "arg":
            print("Child Constructor is calling Parent Argument Constructor")
            super().__init__(42)
        else:
            print("Child Constructor with unknown mode")

def main():
    print("Creating Child Component that calls Parent Default Constructor:")
    child1 = Child()

    print("Creating Child Component that calls Parent Argument Constructor:")
    child2 = Child("arg")

main()
        
