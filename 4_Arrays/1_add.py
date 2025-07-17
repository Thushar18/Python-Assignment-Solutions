def array_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total
numbers = list(map(int,input().split()))
result = array_sum(numbers)
print("The sum of array elements is:",result)
