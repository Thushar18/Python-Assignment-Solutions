def reg_match(s):
    for char in s:
        if char < 'a' and char > 'z':
            return False
    return True

string = input("Enter a String:")
if reg_match(string):
    print("String matches the pattern [a-z]+")
else:
    print("String does not matches the pattern [a-z]+")
