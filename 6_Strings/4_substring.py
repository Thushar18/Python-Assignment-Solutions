def extract_substring(str,start,length):
    result = ""
    i=0
    for char in str:
        if i >= start and i < start + length:
            result += char
        i+=1
    return result

input_str = input("Enter the string:")
start = int(input("Enter the starting index:"))
length = int(input("Enter the number of characters to extarct"))

substring = extract_substring(input_str,start,length)
print("The extracted substring is:",substring)


