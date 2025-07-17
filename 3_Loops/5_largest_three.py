a = int(input())
b = int(input())
c=int(input())

if a>b and a > c:
    largest = a
if b>a and b>c:
    largest = b
else:
    largest = c
print("The Largest Number is:", largest)
