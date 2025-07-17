def remove_element(arr,target):
    result = []
    for i in range(len(arr)):
        if arr[i]!= target:
            result.append(arr[i])
    return result

numbers = list(map(int,input("Enter the array elements:").split()))
target=int(input("Enter the element to remove:"))
updated_elements = remove_element(numbers,target)
print("Updated Elements in the array:",updated_elements)
            
