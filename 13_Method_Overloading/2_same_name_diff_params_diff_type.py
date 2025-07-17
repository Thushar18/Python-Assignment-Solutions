class Printer:
    def display(self,*args):
        if len(args) == 1 and isinstance(args[0],str):
            print(f"Displaying  string: {args[0]}")
        
        elif len(args) == 2 and isinstance(args[0],int) and isinstance(args[1],float):
            print(f"Displaying int and float: {args[0]} and {args[1]}")
        
        else:
            print("Unsupported argument types or count")


def main():
    p = Printer()

    p.display("Hello,Buddies!")

    p.display(12,27.6)

    p.display(7,"Test")

main()