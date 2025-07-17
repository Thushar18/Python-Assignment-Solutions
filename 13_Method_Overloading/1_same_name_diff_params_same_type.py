class Calculator:
    def add(self,*args):
        if len(args) == 2:
            result = args[0] + args[1]
            print(f"Addition of 2 numbers: {args[0]} + {args[1]} = {result}")
        
        elif len(args) == 3:
            result = args[0] + args[1] + args[2]
            print(f"Addition of 3 numbers: {args[0]} + {args[1]} + {args[2]} = {result}")
        
        else:
            print("Invalid number of arguments. Please pass 2 or 3 arguments")

def main():
    calc = Calculator()

    calc.add(20,40)

    calc.add(12,18,45)

    calc.add(7)

main()