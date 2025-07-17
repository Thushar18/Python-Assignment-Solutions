class Operation:
    def process(self,a,b):

        if a==b:
            print(f"Both values are equal:{a} == {b}")
        
        else:
            print(f"Adding values: {a} and {b} = {a + b}")

def main():
    op = Operation()

    op.process(15,15)
    op.process(12,17)

main()