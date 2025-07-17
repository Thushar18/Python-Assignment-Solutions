def second_largest(arr):
    if len(arr) < 2:
        return None
    largest = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    second = None
    for i in range(len(arr)):
        if arr[i] != largest:
            if second is None or arr[i] > second:
                second = arr[i]
    return second

arr = list(map(int,input().split()))
result = second_largest(arr)

if result is not None:
    print("The Second Largest Element is:", result)
else:
    print("The Second Element not exists")