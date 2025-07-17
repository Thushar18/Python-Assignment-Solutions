def reverse_array(arr):
    start = 0
    end = len(arr)-1
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start+=1
        end-=1

    return arr

arr = list(map(int,input().split()))
reversed_array = reverse_array(arr)

print("The Reversed Array is :", reversed_array)