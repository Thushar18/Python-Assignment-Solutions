def remove_duplicates(arr):
    new_arr =[]
    for i in range(len(arr)):
        is_duplicate = False
        for j in range(len(new_arr)):
            if(arr[i] == new_arr[j]):
                is_duplicate = True
                break
        if not is_duplicate:
            new_arr.append(arr[i])
    return new_arr

arr = list(map(int,input().split()))
unique_arr = remove_duplicates(arr)
print("Array after duplicates:",unique_arr)