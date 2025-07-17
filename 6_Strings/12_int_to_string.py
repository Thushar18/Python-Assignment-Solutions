def int_to_string(number):
    if number == 0:
        return '0'
    
    is_negative = False
    while number < 0:
        is_negative = True
        number = -number

    result = ""
    while number > 0:
        digit = number % 10
        result = chr(ord('0')+ digit) + result
        number = number // 10
    
    if is_negative:
        result = "-" + result
    return result

num = int(input("enter a number:"))

str_conversion = int_to_string(num)

print("The converted string is:", str_conversion)
print("Type after conversion:",type(str_conversion))


