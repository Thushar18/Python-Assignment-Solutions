def common_values(arr1,arr2):
    common_val = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                common_val.append(arr1[i])
    return common_val

arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
cmn_values = common_values(arr1,arr2)

if cmn_values:
    print("The Common Values in the array are:",cmn_values)
else:
    print("There are no common values in the array")


