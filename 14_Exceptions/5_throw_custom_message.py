def check_age(age):
    if age < 0:
        raise ValueError("Invalid Age: Age cannot be negative")
    
    elif age < 18:
        raise Exception("Access Denied: You must be 18 or older")
    
    else:
        print("Access Granted: You are Eligible")

def main():
    try:
        user_age = int(input("Enter your age:"))
        check_age(user_age)
    
    except ValueError as ve:
        print("ValueError caught:",ve)
    
    except Exception as e:
        print("Exception caught:",e)

main()