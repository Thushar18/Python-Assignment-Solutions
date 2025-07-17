def contain_elements(arr):
    is_12 = False
    is_23 = False
    for i in range(len(arr)):
        if(arr[i] == 12):
            is_12 = True
        elif(arr[i] == 23):
            is_23 = True
    if is_12 and is_23:
        return True
    else:
        return False
arr= list(map(int,input().split()))
result = contain_elements(arr)

if result:
    print("Both 12 and 23 are present in an array")
else:
    print("Array does not contain both 12 and 23")