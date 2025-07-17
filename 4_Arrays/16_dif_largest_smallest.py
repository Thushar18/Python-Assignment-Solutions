def diff_max_min(arr):
    max_ele = arr[0]
    min_ele = arr[0]
    for i in range(len(arr)):
        if(arr[i] > max_ele):
            max_ele = arr[i]
        elif(arr[i]< min_ele):
            min_ele = arr[i]

    return max_ele - min_ele

arr = list(map(int,input().split()))
difference = diff_max_min(arr)

if difference is not None:
    print("The Difference Between Largest and Smallest elements are:", difference)
else:
    print("Array is Empty")