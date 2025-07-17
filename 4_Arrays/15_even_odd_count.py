def even_odd_count(arr):
    even = 0
    odd = 0
    for i in range(len(arr)):
        if(i%2 == 0):
            even+=1
        else:
            odd+=1

    return even,odd

arr = list(map(int,input().split()))
even_count,odd_count = even_odd_count(arr)
print("The Number of Even Numbers in the Array are:",even_count)
print("The Number of Odd Numbers in the Array are:",odd_count)