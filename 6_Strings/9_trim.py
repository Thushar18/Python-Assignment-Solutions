def custom_strip(s):
    start = 0
    end = len(s) - 1

    while start <= end and s[start] == " ":
        start+=1
    
    while end >= start and s[end] == " ":
        end-=1
    
    result = ""
    for i in range(start,end+1):
        result += s[i]
    
    return result

input_str = input("Enter a string with leading/trailing spaces: ")
trimmed = custom_strip(input_str)

print("Original String: -->" + input_str + "<--")
print("Trimmed String: -->" + trimmed + "<--")



