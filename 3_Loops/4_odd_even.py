numbers = list(map(int,input("Enter numbers separated by space:").split()))
print("Even Numbers:")
for i in numbers:
    if i%2 == 0:
        print(i,end=" ")
print()
print("Odd Numbers:")
for i in numbers:
    if i%2 != 0:
        print(i,end=" ")
