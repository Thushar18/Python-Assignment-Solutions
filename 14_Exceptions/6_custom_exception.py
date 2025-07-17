class InvalidAgeException(Exception):
    def __init__(self,message):
        super().__init__(message)

def validate_age(age):
    if age < 0:
        raise InvalidAgeException("Invalid Age: Age cannot be negative")
    
    elif age < 18:
        raise InvalidAgeException("Access Denied:Must be 18 or older")
    
    else:
        print("Access Granted. Age is Eligible")

def main():
    try:
        age = int(input("enter your age:"))
        validate_age(age)
    
    except InvalidAgeException as e:
        print("Custom Exception Caught:",e)
    
    except ValueError:
        print("Please Enter a Valid Number")

main()


