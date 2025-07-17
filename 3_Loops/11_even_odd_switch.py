num = int(input())
remainder = num % 2
match remainder:
    case 0:
        print(f"{num} is a even number")
    case 1:
        print(f"{num} is a odd number")