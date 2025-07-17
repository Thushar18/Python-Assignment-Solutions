def custom_replace(actual,old_char,new_char):
    result = ""
    for char in actual:
        if char == old_char:
            result += new_char
        else:
            result += char
    return result

input_str = input("Enter the actual string:")
old_char = input("Enter the character to replace:")
new_char = input("Enter the new character:")

replaced_str = custom_replace(input_str,old_char,new_char)

print("Actual String:",input_str)
print("Replaced String:",replaced_str)

