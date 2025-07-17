def insert_pos(arr,ele,pos):
    new_arr = [0] * (len(arr)+1)

    for i in range(len(new_arr)):
        if i < pos:
            new_arr[i] = arr[i]
        elif i == pos:
            new_arr[i] = ele
        else:
            new_arr[i] = arr[i-1]
    
    return new_arr

arr = list(map(int,input().split()))
ele = int(input("Enter the Element:"))
pos = int(input("Enter the position of the element:"))

if 0 <= pos <= len(arr):
    updated_arr = insert_pos(arr,ele,pos)
    print("Array after Insertion :",updated_arr)
else:
    print("Invalid Position!")

