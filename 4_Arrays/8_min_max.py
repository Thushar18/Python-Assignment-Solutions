def min_arr(C):
    min_val = float("inf")
    for num in C:
        if num < min_val:
            min_val = num
    return min_val

def max_arr(C):
    max_val = float("-inf")
    for num in C:
        if num > max_val:
            max_val = num
    return max_val

C = list(map(int,input().split()))
N = len(C)
print("The Minimum Value of Array is :", min_arr(C))
print("The Maximum Value of Array is :", max_arr(C))
