def find_length(str):
    count = 0
    for char in str:
        count += 1
    return count

input_str = input("Enter a String:")
length = find_length(input_str)

print("The length of the string is:",length)