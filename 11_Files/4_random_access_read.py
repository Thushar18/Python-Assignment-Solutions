def read_file_random_access(filename):
    try:
        file = open(filename,"r")
        print("Reading file using random access:")

        print("/n First 10 characters:")
        for _ in range(10):
            char = file.read(1)
            if not char:
                break
            print(char,end="")
        
        pos = file.tell()
        print(f"Current file pointer position: {pos}")

        file.seek(5)
        print("\n Reading 10 characters from byte position 5:")
        for _ in range(10):
            char = file.read(1)
            if not char:
                break
            print(char,end="")
    except FileNotFoundError:
        print("File Not Found, please check the file path")
    except IOError:
        print("An Error occured while accessing the file")

filename = input("Enter the filename or path:")
read_file_random_access(filename)

