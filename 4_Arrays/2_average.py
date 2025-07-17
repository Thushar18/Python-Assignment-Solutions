def find_avg(nums):
    if len(nums) == 0:
        return 0
    total_avg = 0
    for i in nums:
        total_avg += i
    avg = total_avg / len(nums)
    return avg
arr = list(map(int,input().split()))
result = find_avg(arr)
print("The result of the integers is :", result)