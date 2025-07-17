def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
        
    return duplicates
    
arr=list(map(int,input().split()))
dup_values = find_duplicates(arr)
if dup_values:
    print("Duplicates are found in the array:",dup_values)
else:
    print("There are no duplicates in the array")

