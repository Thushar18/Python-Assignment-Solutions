gender = input("Enter your gender(M/F)")
match gender:
    case 'M':
        print("Male")
    case 'F':
        print("Female")
    case _:
        print(" Invalid Input Please enter M or F")