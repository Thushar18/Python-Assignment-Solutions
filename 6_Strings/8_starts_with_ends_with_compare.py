def starts_with(string,prefix):
    if len(prefix) > len(string):
        return False
    for i in range(len(prefix)):
        if string[i] != prefix[i]:
            return False
    return True

def ends_with(string,suffix):
    if len(suffix) > len(string):
        return False
    offset = len(string) - len(suffix)
    for i in range(len(suffix)):
        if string[ offset + i] != suffix[i]:
            return False
    return True

def compare_to(string1,string2):
    min_len = len(string1) if len(string1) < len(string2) else len(string2)
    for i in range(min_len):
        if string1[i] != string2[i]:
            return ord(string1[i]) - ord(string2[i])
    return len(string1) - len(string2)

main_str = input("enter the main string:")
prefix = input("enter the prefix to check:")
suffix = input("enter the suffix to check:")
compare_str = input("enter another string to compare:")

if starts_with(main_str,prefix):
    print("The string starts with prefix")
else:
    print("The string does not starts with prefix")

if ends_with(main_str,suffix):
    print("The string ends with suffix")
else:
    print("The string does not ends with suffix")

result = compare_to(main_str,compare_str)
if result == 0:
    print("Both strings are equal")
elif result < 0:
    print("The main string is lexicographically smaller")
else:
    print("The main string is lexicographically greater")




