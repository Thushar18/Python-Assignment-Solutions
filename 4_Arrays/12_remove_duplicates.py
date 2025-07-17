def remove_duplicates(arr):
    result = []
    for i in range(len(arr)):
        is_duplicate = False
        for j in range(i):
            if arr[i] == arr[j]:
                is_duplicate = True
                break
        if not is_duplicate:
            result.append(arr[i])
    return result

arr=list(map(int,input().split()))
updated_values = remove_duplicates(arr)

print("Updated elements in the array are:",updated_values)