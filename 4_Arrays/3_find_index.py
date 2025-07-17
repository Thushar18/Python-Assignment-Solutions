def find_index(arr,target):
    for index in range(len(arr)):
        if(arr[index]== target):
            return index
    return -1
numbers = list(map(int,input().split()))
target = int(input("Enter the target element:"))
result = find_index(numbers,target)

if result != -1:
    print("The Element is found at the index", result)
else:
    print("The Element is not found")