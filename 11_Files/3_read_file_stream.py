def read_file_stream(filename):
    try:
        file = open(filename,'r')
        print("Reading file contents character by character:")

        while True:
            char = file.read(1)
            if not char:
                break
            print(char,end="")
        
        file.close()
        print("\n File Reading Completed")
    
    except FileNotFoundError:
        print("File not found, Please check the file name")
    
    except IOError:
        print("An Error occured while reading the file")

filename = input("Enter the filename or path:")
read_file_stream(filename)

