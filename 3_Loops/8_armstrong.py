num = int(input("Enter a number:"))

a = num
n=len(str(num))
temp = num
armstrong_sum = 0
while temp > 0:
    digit = temp % 10
    armstrong_sum += digit ** n
    temp //= 10
if(armstrong_sum == a):
    print(f"{a} is armstrong number")
else:
    print(f"{a} is not armstrong number")

