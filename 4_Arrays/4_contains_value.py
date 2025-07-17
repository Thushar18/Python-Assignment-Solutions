def contains_value(arr,target):
    for element in arr:
        if element == target:
            return True
    return False

numbers = list(map(int,input().split()))
target=int(input())
result = contains_value(numbers,target)

if(result):
    print("Element contains value in the array")
else:
    print("Element does not contain valur in the array")
