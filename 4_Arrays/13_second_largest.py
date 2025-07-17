def second_largest(arr):
    if len(arr)<2:
        return None
    first = second = float("-inf")
    for nums in arr:
        if nums > first:
            second = first
            first = nums
        elif nums > second and nums != first:
            second = nums
    if second == float("-inf"):
        return None
    return second
arr=list(map(int,input().split()))
result = second_largest(arr)
if result is not None:
    print("The Second Largest Element is:", result)
else:
    print("The Second Largest Element is not found")