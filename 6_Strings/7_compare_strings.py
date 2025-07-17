def compare_strings(str1,str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True

string1 = input("Enter the first string")
string2 = input("Enter the second string")
if compare_strings(string1,string2):
    print("The strings are equal")
else:
    print("The strings are not equal")
