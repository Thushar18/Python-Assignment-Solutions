def to_uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char

    return result

def to_lowercase(str):
    result = ""
    for char in str:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

input_str = input("Enter input string:")

uppercase_str = to_uppercase(input_str)
lowercase_str = to_lowercase(input_str)

print("Uppercase:",uppercase_str)
print("Lowercase:",lowercase_str)